from fetchers import GitFetcher, ZipFetcher

class Assembler(object):
    """The source code assember."""
    def __init__(self, projects, destination, extra):
        """
        :type projects:     list[dict[str, str]]
        :type destination:  str
        :type extra:        dict[str, str] 
        """
        self.destination    = destination
        self.extra          = extra
        self.projects       = projects
        
    def assemble(self):
        """Release the gerbles!"""
        for project in self.projects:
            if project["provider"] == "git":
                fetcher = GitFetcher(self.destination, project)
                fetcher.fetch()
            elif project["provider"] == "zip":
                fetcher = ZipFetcher(self.destination, project)
                fetcher.fetch()
