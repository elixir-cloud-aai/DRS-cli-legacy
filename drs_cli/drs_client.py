"""
Client script for the GA4GH data repository schema
"""
from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS


#connexion stub runs on port 5000
connexion_url = 'http://127.0.0.1:5000/ga4gh/drs/v1'

#specify config for bravado
DEFAULT_CONFIG = {'validate_responses':False,
                  'validate_requests':False,
                  'formats':DEFAULT_FORMATS['int64']}

#create a client using bravado
class Client:
    def __init__(self, url=connexion_url, config=DEFAULT_CONFIG):
        self._config = config
        config['formats'] = [DEFAULT_FORMATS['int64']]
        swagger_path = '{}/swagger.json'.format(url.rstrip('/'))
        
        self.models = SwaggerClient.from_url(swagger_path, config=config)
        self.client = self.models.DataRepositoryService
            
    def GetAccessURL(self,object_id,access_id):
        return self.client.GetAccessURL(object_id=object_id,access_id=access_id).result()
        
    def GetBundle(self,bundle_id):
        return self.client.GetBundle(bundle_id=bundle_id).result()
        
    def GetObject(self,object_id):
        return self.client.GetObject(object_id=object_id).result()
        
    def GetServiceInfo(self):
        return self.client.GetServiceInfo().result()

if __name__ == '__main__' :
    
    #create an object for the Client class
    client = Client()
    c = client.client
    
    
    #client.GetAccessURL(123,"temp")
    #client.GetServiceInfo()
    #client.GetObject(123)
    client.GetBundle(213)