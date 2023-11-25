
import requests
import json

class ForloopClient:
    def __init__(self, key=None, secret=None, url=None):
        self.key = key
        self.secret = secret

        if url:
            self.url = url
        else:
            self.url = "https://www.forloop.ai"
            
    def execute_pipeline(self, user_email: str, pipeline_name: str):
        url = f'{self.url}/api/v1/execute_pipeline'
        
        payload = {
            "name": pipeline_name,
            "user_email": user_email
        }
        
        response = requests.post(url, json=payload)
        
        return response
    
    def __get_nodes(self,pipeline):
        response=requests.get(self.url+"/api/v1/nodes")
        print(response,response.content)
        
        result=response.json()["results"]
        return(result)

    def __analyze_data(self,filename):
        payload={"filename":filename}
        response=requests.post(self.url+"/api/v1/analyze_data",data=json.dumps(payload))
        result=response.json()
        
        return result

    def __clean_data(self,filename):
        payload={"filename":filename}
        response=requests.post(self.url+"/api/v1/clean_data",data=json.dumps(payload))
        result=response.json()
        
        return result
    
    def __run_python_script(self,filename,dir_path):        
        payload={"filename":filename,"dir_path":dir_path}
        
        response=requests.post(self.url+"/api/v1/run_python_script",data=json.dumps(payload))
        result=response.json()
        
        return result

    