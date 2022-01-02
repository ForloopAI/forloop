
import requests
import json

class ForloopClient:
    def __init__(self, key=None, secret=None, url=None):
        self.key = key
        self.secret = secret
        #self.session = requests.Session()

        if url:
            self.url = url
        else:
            self.url = "https://www.forloop.ai"

    
    def get_nodes(self,pipeline):
        response=requests.get(self.url+"/api/v1/nodes")
        print(response,response.content)
        
        result=response.json()["results"]
        return(result)


    def analyze_data(self,filename):
        payload={"filename":filename}
        response=requests.post(self.url+"/api/v1/analyze_data",data=json.dumps(payload))
        
        
        #print("RESPONSE",response,response.content)
        
        
        result=response.json()#["results"]
        return(result)


    def clean_data(self,filename):
        payload={"filename":filename}
        response=requests.post(self.url+"/api/v1/clean_data",data=json.dumps(payload))
        
        
        result=pd.read_pickle("C:\\Users\\EUROCOM\\Documents\\Git\\ForloopAI\\forloop_platform_dominik\\cleaned_data.pkl")
        return(result)
    
    
    def run_python_script(self,filename,dir_path):
        #dir_path="C:\\Users\\EUROCOM\\Documents\\Git\\ForloopAI\\forloop_api"
        
        payload={"filename":filename,"dir_path":dir_path}
        
        response=requests.post(self.url+"/api/v1/run_python_script",data=json.dumps(payload))
        
        
        print("RESPONSE",response,response.content)
        
        
        result=response.json()#["results"]
        return(result)


    
    



################# OLDER ##################
import pandas as pd
from idfops.pandas_operations import read_spreadsheet

#Package functions
def load_df(filename):
    try:
        df=read_spreadsheet(filename)[0]
    except FileNotFoundError as e:
        print("File was not found")
        df=None
    return(df)


def send_data_to_forloop(df):
    """TODO: Implementation"""
    pass


def import_batch_data():
    """
    Loading data from batches coming from the platform
    TODO: Implementation
    """
    pass