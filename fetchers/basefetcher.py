class BaseFetcher(object):
    """Common functionality for a fetcher"""
    
    def __init__(self, project_base, params):
        """
        :type project_base: str
        :type params: dict[str, str]
        """
        self.project_base = project_base
        self.source = params["source"]
        
        # Calculate the detination
        self.destination = self.project_base
        if params.get("destination"):
            self.destination += "/" + params.get("destination")
            
        # De we have a specified rename for the folder?
        self.rename = None
        if params.get("rename"):
            self.rename = params.get("rename")
