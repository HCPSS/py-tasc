import os
from patcherinterface import PatcherInterface

class PatchPatcher(PatcherInterface):
    """A class for applying patches via a patch file"""
    
    def __init__(self, patch_base):
        """
        :type patch_base: str
        """
        self.patch_base = patch_base
    
    def patch(self, project_base, destination, source):
        """Perform the patch
        :type project_base: str
        :type destination:  str
        :type source:       str
        """
        source      = self.patch_base + "/" + source
        destination = project_base + "/" + destination
        
        os.system("patch --input={0} {1}".format(source, destination))
