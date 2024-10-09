import os
import datetime
import json
import requests

from api.omdb import OMDb_API

from flask import Blueprint, render_template, request
import sqlalchemy

class ApiRoutes:
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling API endpoints
    """
    blueprint = Blueprint('api', __name__)
    
    """
    The external API to make outbound calls against
    
    TODO: Investigate being able to instance blueprints
          so this can be injected into the instance
          instead of all instances relying on this global
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
    @blueprint.route('/movies/search', methods = ['POST'])
    def handle_search_endpoint(): # Get Movies
        if request.method != 'POST':
            return 'Method Not Allowed', 405
        
        endpoint = ApiRoutes.omdb.endpoints.search
        
        endpoint.params.apikey = os.environ.get('APPLICATION_OMDBAPI_KEY')
        endpoint.params.i      = request.form.get('imdb_id')
        endpoint.params.t      = request.form.get('movie_title_query')
        endpoint.params.type   = request.form.get('result_type')
        endpoint.params.y      = request.form.get('release_year')
        endpoint.params.plot   = request.form.get('plot_length')
        
        connection = ApiRoutes.omdb.exec(endpoint)
        
        response = connection.getresponse()
    
    @blueprint.route('/movie/image', methods = ['POST'])
    def handle_image_endpoint(): # Get Movie Image
        if request.method != 'POST':
            return 'Method Not Allowed', 405
        
        endpoint = ApiRoutes.omdb.endpoints.image
        
        endpoint.params.apikey = os.environ.get('APPLICATION_OMDBAPI_KEY')
        endpoint.params.s      = request.form.get('movie_title_query')
        endpoint.params.type   = request.form.get('result_type')
        endpoint.params.y      = request.form.get('release_year')
        endpoint.params.page   = request.form.get('page')
        
        connection = ApiRoutes.omdb.exec(endpoint)
        
        response = connection.getresponse()
    
    # TODO: For a given user, group saves done close together into a single transaction,
    #       instead of having multiple seperate inserts into the database in succession
    #       for a given user saving many movies at a time as they click on each movie's
    #       favorite button one by one. Maybe can do this on the frontend for now, but
    #       would be risky if the user's session ends. Should be done in the app backend
    #
    @blueprint.route('/<user_id>/movies/save', methods = ['POST'])
    def saveFavoriteMovies(): # TODO: Should accept saving multiple movies
                              #       I'm not sure yet if the frontend will
                              #       be sending more than one at a time, however
        
        if request.method != 'POST':
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
    
    @blueprint.route('/<user_id>/movies/favorites', methods = ['POST'])
    def getFavoriteMovies(user_id):
        if request.method != 'POST':
            return 'Method Not Allowed', 405
        
        with self.database.engine.connect() as connection:
            
            """
            TODO: Get User's Movies with a JOIN on Users_Movies for a given user id, using the model
                  Here's the sql equivalent operation:
                  
                  SELECT *
                      FROM Moive
                  LEFT OUTER JOIN Users_Movies
                      ON Movie.id = Movies_Users.movie_id
                      AND Movies_Users.user_id = {user_id}
            """
            
            # TODO: Iterate over movies and return appropriate frontend data
            #for movie in movies:
            #    print(f' - { movie }')
            
            #return movie_data, 200
            
            pass
