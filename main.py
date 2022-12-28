##############################################
# DATA PROPERTIES
from datetime import datetime
class Serializable:
    def as_dict(self, obj = None):
        ret = {}
        if obj != None:
            read = obj.__dict__
        else:
            read = self.__dict__

        for key in read:
            value = read[key]
            if "data." in str(type(value)):
                ret[key] = self.as_dict(obj=value)
            else:
                ret[key] = value
        return ret

class Settable:
    def __setitem__(self,k,v):
        setattr(self,k,v)
        
    def __getitem__(self,k):
        return getattr(self, k)
    
    def set(self,obj: object):
        if obj == None:
            return
        
        for key in obj:
            self[key] = obj[key]

# timestamp
def get_timestamp() -> str:
    return datetime.now().isoformat()

##############################################
# ENV CONFIGURATION
from dotenv import load_dotenv
from os import environ as env
class Configuration(Serializable,Settable):

    def __init__(self) -> None:
        load_dotenv()
        self.load()

    # LOAD CONFIGURATION
    def load(self):
        variables = self.getVariables()
        for variable in variables:
            self[variable] = env.get(variable)
    
    # GET VARIABLES NAMES
    def getVariables(self):
        variables = []
        with open(".env") as f:
            lines = f.readlines()
        for line in lines:
            if line[0] != "#" and line.strip() != "":
                variables.append(line.strip().split("=")[0])
        return variables