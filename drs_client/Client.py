"""
Client script for the GA4GH data repository schema
"""

from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS


# specify config for bravado
DEFAULT_CONFIG = {
    "validate_responses": False,
    "validate_requests": False,
    "formats": DEFAULT_FORMATS["int64"],
}


# create a client using bravado
class Client:
    def __init__(self, url, config=DEFAULT_CONFIG):
        self._config = config
        config["formats"] = [DEFAULT_FORMATS["int64"]]
        swagger_path = "{}/swagger.json".format(url.rstrip("/"))

        self.models = SwaggerClient.from_url(swagger_path, config=config)
        self.client = self.models.DataRepositoryService

    def GetAccessURL(self, object_id, access_id):
        return self.client.GetAccessURL(
            object_id=object_id, access_id=access_id
        ).result()

    def GetBundle(self, bundle_id):
        return self.client.GetBundle(bundle_id=bundle_id).result()

    def GetObject(self, object_id):
        return self.client.GetObject(object_id=object_id).result()

    def GetServiceInfo(self):
        return self.client.GetServiceInfo().result()


if __name__ == "__main__":

    # An example of how to create & use the client

    # create an object using the Client class
    client = Client(url="http://193.166.24.114/ga4gh/drs/v1")
    c = client.client
    response = client.GetObject("a001")
    print(response)
