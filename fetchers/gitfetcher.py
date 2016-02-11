import tempfile, shutil, os
from basefetcher import BaseFetcher
from subprocess import call
from distutils.dir_util import copy_tree

class GitFetcher(BaseFetcher):
    """Fetch project from git"""
    
    def __init__(self, project_base, params):
        """
        :type project_base: str
        :type params: dict[str, str]
        """
        
        BaseFetcher.__init__(self, project_base, params)
        self.tag = params.get("tag", "master")
    
    def fetch(self):
        """Fetch the files from git"""
        
        # We need a place to store the repo temporarily
        templocation = tempfile.mkdtemp()
        
        # Clone the repo        
        call(["git", "clone", self.source, templocation])
        
        # Checkout the correct tag or branch
        call(["git", "-C", templocation, "checkout", self.tag])
        
        # Delete the .git folder and .gitignore file
        shutil.rmtree(templocation + "/.git")
        if os.path.exists(templocation + "/.gitignore"):
            os.remove(templocation + "/.gitignore")
            
        # Move the repo into the final position 
        destination = self.destination
        if self.rename:
            destination = destination + "/" + self.rename
            
        copy_tree(templocation, destination)
        
        # Clean up
        shutil.rmtree(templocation)
