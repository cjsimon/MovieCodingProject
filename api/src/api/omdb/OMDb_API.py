import os

from api import API
from .endpoints.image import endpoint as image_endpoint
from .endpoints.search import endpoint as search_endpoint
from flask_app.libs import attrs

class OMDb_API(API):
    def __init__(self, endpoints=None):
        super().__init__(endpoints=attrs({
                'search': search_endpoint(),
                'image':  image_endpoint(),
            }) if endpoints is None else endpoints
        )
