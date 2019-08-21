"""
Client script for the GA4GH data repository schema
"""

from typing import List

from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS


# specify config for bravado
DEFAULT_CONFIG = {
    "validate_responses": False,
    "validate_requests": False,
    "formats": [DEFAULT_FORMATS["int64"]],
}


# create a client using bravado
class Client:
    def __init__(self, url, config=DEFAULT_CONFIG):

        swagger_path = "{url}/swagger.json".format(url=url.rstrip("/"))
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

    def updateDatabaseObjects(self, clear: bool, objects: List):
        """
        :param clear: if the database should be cleared or not
        :param objects: a list of dicts( which should be the drs objects)
        :return: a list of available object_id's on the drs_db
        """

        UpdateObjects = self.models.get_model("UpdateObjects")

        db_objects = []
        for obj in objects:
            if not {"id", "size", "created", "access_methods"}.issubset(obj):
                print("provide " + str({"id", "size", "created", "access methods"} - set(obj.keys()))+ " for object")
            else:
                db_object = self.models.get_model("Object")
                db_objects.extend([db_object._from_dict(obj)])

        if db_objects == []:
            print("No valid objects found in request")
            return None

        request = UpdateObjects(clear_db=clear, data_objects=db_objects)
        response = self.client.updateDatabaseObjects(body=request).result()
        return response.objects
