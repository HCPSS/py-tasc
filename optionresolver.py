import optparse, yaml, json

class OptionResolver(object):
    """Resolve user input options"""
    
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.set_options()
        
    def set_options(self):
        """Use optparser to manage options"""
        
        self.parser.add_option(
            "--manifest", "-m", 
            help    = "The location of the manifest file.", 
            default = "./manifest.yml")
        
        self.parser.add_option(
            "--destination", "-d", 
            help    = "Where to assemble the code.", 
            default = ".")
        
        self.parser.add_option(
            "--extra-parameters", "-e", 
            help = "A JSON encoded string with extra parameters.")
        
    def parse(self):
        """Return the raw parsed user supplied values
        :rtype: dict[str, str]
        """
        
        return self.parser.parse_args()[0]
    
    def manifest_location(self):
        """Return the location of the manifest file
        :rtype: str
        """
        
        return self.parse().manifest
    
    def manifest(self):
        """Get the parsed values from the manifest
        :rtype: dict[str, mixed]
        """
        
        with open(self.manifest_location(), "r") as stream:
            yamlstring = stream.read()
            
            # Allow token replacements
            params = self.extra_parameters()
            if params:
                yamlstring = yamlstring.format(**params)
            
            return yaml.load(yamlstring)
    
    def destination(self):
        """Get the assembly location
        :rtype: str
        """
        
        return self.parse().destination
    
    def extra_parameters(self):
        """Get extra parameters
        :rtype: dict[str, str]
        """
        params_string = self.parse().extra_parameters
        
        if params_string:
            return json.loads(self.parse().extra_parameters)        
