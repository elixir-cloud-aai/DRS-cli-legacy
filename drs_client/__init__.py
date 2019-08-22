"""
Client for the mockup GA4GH Data Repository Service `mock-DRS`.
"""
from typing import List

from bravado.client import SwaggerClient, CallableOperation
from bravado_core.formatter import DEFAULT_FORMATS

# Bravado configuration
DEFAULT_CONFIG = {
    "validate_responses": False,
    "validate_requests": False,
    "headers": None,
    "formats": [DEFAULT_FORMATS["int64"]],
    "include_missing_properties": True,
}


class Client:
    """Client for mock-DRS service."""
    def __init__(self, url, config=DEFAULT_CONFIG):
        swagger_path = "{url}/swagger.json".format(url=url.rstrip("/"))
        self.models = SwaggerClient.from_url(
            swagger_path,
            config=config
        )
        self.client = self.models.DataRepositoryService


    def getObject(
        self,
        object_id,
        timeout: float = 3,
    ):
        return self.client.GetObject(
            object_id=object_id,
        ).result(timeout=timeout)


    def updateDatabaseObjects(
        self,
        objects: List,
        clear_db: bool = False,
        timeout: float = 3,
    ):
        """
        Updates database with the specified objects.

        :param objects: A list of DRS `Object` model dictionaries.
        :param clear_db: Set to `True` if the database should be cleared before
                adding the objects.

        :return: A list of identifiers of objects available in the DRS
                database.
        """
        UpdateObjects = self.models.get_model("UpdateObjects")
        db_objects = []
        for obj in objects:
            db_object = self.models.get_model("Object")
            db_objects.extend([db_object._from_dict(obj)])
        request = UpdateObjects(
            clear_db=clear_db,
            data_objects=db_objects
        )
        response = self.client.updateDatabaseObjects(
            body=request
        ).result(timeout=timeout)
        return response.objects
