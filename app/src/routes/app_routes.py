import os

from api.internal import Internal_API

from libs.flask_app.configuration import Config
from flask import Blueprint, render_template, request, send_from_directory

"""
The pages directory relative to the webroot

TODO: Blueprint routes don't easily accept self references.
      Just use the static Config.BASE_PATH for now instead
      of the one from the parent app instance
"""
pages_dir = 'pages'
pages_path = os.path.join(Config.BASE_PATH, pages_dir)

class AppRoutes:
    """
    WebApp Routes
    """
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling web pages
    """
    blueprint = Blueprint('app', __name__)
    
    """
    The API for the MovieManager project
    
    TODO: Investigate being able to instance blueprints
          so this can be injected into the instance
          instead of all instances relying on this global
    """
    api = Internal_API()
    
    def __init__(self, parent_app, parent_database=None):
        """ App Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
    
    @blueprint.route('/api/search', methods=['POST'])
    def process_search_route():
        response_data = None
        
        if request.method == 'POST':
            try:
                response_data = process_search_request(request)
            except:
                # TODO: Pass exceptions to error log
                pass
        
        return response_data, 200 if response_data is not None else 'Internal Service Error', 500
    
    @blueprint.route('/api/image', methods=['POST'])
    def process_image_route():
        response_data = None
        
        if request.method == 'POST':
            try:
                response_data = image_process_image_request(request)
            except:
                # TODO: Pass exceptions to error log
                pass
            
            return response_data, 200 if response_data is not None else 'Internal Service Error', 500
        
        else:
            
            return 'Method Not Allowed', 405
    
    def process_search_request(request):
        search = AppRoutes.api.endpoints.search
        
        # Server                        = Client
        search.params.imdb_id           = request.form.get('imdb-id')
        search.params.movie_title_query = request.form.get('media-title')
        search.params.result_type       = request.form.get('media-type')
        search.params.release_year      = request.form.get('media-year')
        search.params.plot_length       = request.form.get('plot-length')
        
        search_response = AppRoutes.api.exec(search).getresponse()
        
        # TODO: Look into how expensive it is to pass whole responses like this.
        #       It would likely be much cheaper to do the work inline here instead
        return process_search_respose(search_response)
    
    def process_search_respose(search_response):
        return search_response
    
    def process_image_request(request):
        image = AppRoutes.api.endpoints.image
        
        # Server                        = Client
        search.params.imdb_id           = request.form.get('imdb-id')
        search.params.movie_title_query = request.form.get('media-title')
        search.params.result_type       = request.form.get('media-type')
        search.params.release_year      = request.form.get('media-year')
        search.params.plot_length       = request.form.get('plot-length')
        
        image_response = api.exec(image).getresponse()
        
        # TODO: Look into how expensive it is to pass whole responses like this.
        #       It would likely be much cheaper to do the work inline here instead
        return process_image_respose(image_response)
    
    def process_image_respose(image_response):
        return image_response
