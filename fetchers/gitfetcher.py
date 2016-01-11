import tempfile, shutil, os
from basefetcher import BaseFetcher
from git import Repo
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
        Repo.clone_from(self.source, templocation, branch=self.tag)
        
        # Delete the .git folder and .gitignore file
        shutil.rmtree(templocation + "/.git")
        if os.path.exists(templocation + "/.gitignore"):
            os.remove(templocation + "/.gitignore")
            
        # Move the repo into the final position        
        copy_tree(templocation, self.destination)
        
        # Clean up
        shutil.rmtree(templocation)
