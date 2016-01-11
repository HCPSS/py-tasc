import requests, zipfile, StringIO
from basefetcher import BaseFetcher

class ZipFetcher(BaseFetcher):
    """Fetch projects from remote zip files"""
    
    def fetch(self):
        """Fetch remote zip file and extract it to the destination"""
        
        request = requests.get(self.source)
        zip = zipfile.ZipFile(StringIO.StringIO(request.content))
        zip.extractall(path=self.destination)
