import os

from api import API
from .endpoints.image import endpoint as image_endpoint
from .endpoints.search import endpoint as search_endpoint

from libs import attrs

class OMDb_API(API):
    """
    OMDb API bindings
    
    https://www.omdbapi.com/
    """
    
    def __init__(self, endpoints=None):
        super().__init__(endpoints=endpoints if endpoints is not None else attrs({
            'search': search_endpoint(),
            'image':  image_endpoint(),}))
