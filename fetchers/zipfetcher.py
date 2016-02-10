import requests, zipfile, StringIO, shutil
from basefetcher import BaseFetcher

class ZipFetcher(BaseFetcher):
    """Fetch projects from remote zip files"""
    
    def fetch(self):
        """Fetch remote zip file and extract it to the destination"""
        
        request = requests.get(self.source)
        zip = zipfile.ZipFile(StringIO.StringIO(request.content))
        location = zip.extractall(path=self.destination)
        
        # The very first thing extracted should be the parent folder. But it
        # has a slash at the end (because it's a directory). So, let's 
        # format it a little.
        original_name = zip.infolist()[0].filename.split("/")[0]
        if self.rename and self.rename != original_name:
            shutil.move(self.destination+"/"+original_name, self.destination+"/"+self.rename)

