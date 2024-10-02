from flask import Blueprint, render_template

import datetime
import http.client
import json
import requests
import sqlalchemy

class Routes:
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling API endpoints
    """
    blueprint = Blueprint('api', __name__)
    
    def __init__(self, parent_app, parent_database=None):
        """ API Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
    
    # TODO: Create appropriate routes according to the external api.
    #       Don't forget to whitelist their ip as a firewall egress rule
    #
    @blueprint.route('/', methods = ['GET', 'POST'])
    def index():
        with self.database.engine.connect() as connection:
            connection = http.client.HTTPSConnection('{base api url goes here}')
            
            # TODO: Get appropriate route with params and required auth for api usage
            connection.request('GET', '/v1/movies/demoroute?param=' + someparam, None, headers: {
                'Accept':        'application/json'
                'Authorization': 'Bearer 1234SomeBearerAuthToken'
            })
            response = connection.getresponse()
            
            json_results = response.read()
            results = json.loads(json_results)
            
            # TODO
            response = {
                'status': status,
                'message': message,
            }
            
            return jsonify(response), 200
