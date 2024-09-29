from flask import Blueprint, render_template

import datetime
import http.client
import json
import random
import requests
import sqlalchemy

class Routes:
    
    def __init__(self, parent_app, parent_database) {
        """ Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
        
        """ The blueprint for defining and handling API endpoints """
        self.api_blueprint = Blueprint('api', __name__)
    }
    
    @app_blueprint.route('/', methods = ['GET', 'POST'])
    def index():
        return 
