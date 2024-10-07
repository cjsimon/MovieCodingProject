import os

from api import API
from .endpoints.image import endpoint as image_endpoint
from .endpoints.search import endpoint as search_endpoint

from libs import attrs
from libs import ServiceDiscovery

class Internal_API(API):
    """
    The internal MovieManager project API
    """
    
    def __init__(self, endpoints=None):
        super().__init__(endpoints=endpoints if endpoints is not None else attrs({
            'search': search_endpoint(),
            'image':  image_endpoint(),}))
    
    def exec(endpoint, connection=None, url=None, route=None, params=None, method=None):
        """
        Override the default connection to get the internal api host using ServiceDiscovery.
        This is done at request-time so that a host address change can be picked up seamlessly
        """
        
        connection = connection if connection is not None else http.client.HTTPSConnection(host=ServiceDiscovery.getApiHost())
        
        return super().exec(endpoint, connection, url=None, route=None, params=None, method=None)
