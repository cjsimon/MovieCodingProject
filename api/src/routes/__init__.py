from api.omdb import OMDb_API
from flask import Blueprint, render_template

import datetime
import json
import requests
import sqlalchemy

class Routes:
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling API endpoints
    """
    blueprint = Blueprint('api', __name__)
    
    """
    The internal API to make outbound calls against
    """
    omdb = OMDb_API()
    
    def __init__(self, parent_app, parent_database=None):
        """ API Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
    
    # TODO: Create appropriate routes according to the external api.
    #       Don't forget to whitelist their ip as a firewall egress rule
    #
    @blueprint.route('/search', methods = ['POST'])
    def search():
        if request.method is not 'POST':
            return 'Method Not Allowed', 405
        
        endpoint = omdb.endpoint.search
        
        endpoint.params.apikey = os.environ.get('APPLICATION_OMDBAPI_KEY')
        endpoint.params.i      = request.form.get('imdb_id')
        endpoint.params.t      = request.form.get('movie_title_query')
        endpoint.params.type   = request.form.get('result_type')
        endpoint.params.y      = request.form.get('release_year')
        endpoint.params.plot   = request.form.get('plot_length')
        
        connection = omdb.exec(endpoint)
        
        response = connection.getresponse()
    
    @blueprint.route('/image', methods = ['POST'])
    def image():
        if request.method is not 'POST':
            return 'Method Not Allowed', 405
        
        endpoint = omdb.endpoint.image
        
        endpoint.params.apikey = os.environ.get('APPLICATION_OMDBAPI_KEY')
        endpoint.params.s      = request.form.get('movie_title_query')
        endpoint.params.type   = request.form.get('result_type')
        endpoint.params.y      = request.form.get('release_year')
        endpoint.params.page   = request.form.get('page')
        
        connection = omdb.exec(endpoint)
        
        response = connection.getresponse()
        pass
    
    # TODO: For a given user, group saves done close together into a single transaction,
    #       instead of having multiple seperate inserts into the database in succession
    #       for a given user saving many movies at a time as they click on each movie's
    #       favorite button one by one. Maybe can do this on the frontend for now, but
    #       would be risky if the user's session ends. Should be done in the app backend
    #
    @blueprint.route('/movies/save', methods = ['POST'])
    def saveMovies(): # TODO: Should accept saving multiple movies
                      #       I'm not sure yet if the frontend will
                      #       be sending more than one at a time, however
        
        if request.method is not 'POST':
            return 'Method Not Allowed', 405
        
        with self.database.engine.connect() as connection:
            session = self.database.session
            movies = session.query(Movies).all()
            
            # TODO
            #session.add(Movie)
            
            #json_results = response.read()
            #results = json.loads(json_results)
            
            #response = {
            #    'status': status,
            #    'message': message,
            #}
            
            #return jsonify(response), 200
            
            return 'Saved', 200
    
    @blueprint.route('/movies/get', methods = ['POST'])
    def getFavoriteMovies():
        if request.method is not 'POST':
            return 'Method Not Allowed', 405
        
        with self.database.engine.connect() as connection:
            pass
            # TODO: Get User_Movies for a given user id, using the model
            #session.add(Movie)
            
            # TODO: Iterate over movies and return appropriate frontend data
            #for movie in movies:
            #    print(f' - { movie }')
            
            #return movie_data, 200
