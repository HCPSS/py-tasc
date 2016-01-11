class PatchManager(object):
    """Manage patcher methods"""
    
    def __init__(self, patches, project_base):
        """
        :type patches:        list[str]
        :type project_base:   str
        """
        
        self.patchers       = {}
        self.patches        = patches
        self.project_base   = project_base
    
    def add_patcher(self, name, patcher):
        """Add a Patcher to the list of patchers
        :type name:     str
        :type patcher:  PatcherInterface
        """
        self.patchers[name] = patcher
        
    def get_patcher(self, name):
        """Get a patcher by name
        :type patcher: str
        :rtype: PatcherInterface
        """
        return self.patchers[name]
    
    def patch(self):
        """Perform the patches"""
        for patch in self.patches:
            patcher = self.get_patcher("patch_file")
            patcher.patch(self.project_base, patch["destination"], patch["source"])
    