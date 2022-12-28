from dotenv import load_dotenv
from os import environ as env
from main import Serializable,Settable

class Configuration(Serializable,Settable):
    def __init__(self) -> None:
        self.loaded = False
        if not self.loaded:
            load_dotenv()
            self.loaded = True
        self.variables = []

    # LOAD CONFIGURATION
    def load(self):
        self.getVariables()
        for variable in self.variables:
            self[variable] = env.get(variable)
    
    # GET VARIABLES NAMES
    def getVariables(self):
        self.variables = []
        with open(".env") as f:
            lines = f.readlines()
        for line in lines:
            self.variables.append(line.strip().split("=")[0])

