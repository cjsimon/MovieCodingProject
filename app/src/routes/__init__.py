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

class Routes:
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
    
    """
    A static list of available pages within the webapp
    
    TODO: Move to App instead of defining here in routes?
    """
    Pages = {
        page: '%(page)s/%(page)s.html' % {
            'base_dir': pages_path,
            'page': page
        } for page in [
            'Search',
        ]
    }
    
    def __init__(self, parent_app, parent_database=None):
        """ App Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
    
    @blueprint.route('/static/<path:filename>')
    def process_static_asset_route(filename):
        """
        Appropriately serve any publicly accessible static asset files
        """
        
        mimetype = None
        
        if filename.endswith('.js') or filename.endswith('.mjs'):
            mimetype = 'text/javascript'
        
        return send_from_directory(filename=filename, mimetype=mimetype)
    
    @blueprint.route('/', methods=['GET', 'POST'])
    @blueprint.route('/search', methods=['GET', 'POST'])
    def process_search_route():
        response_data = None
        
        if request.method == 'POST':
            try:
                response_data = process_search_request(request)
            except:
                # TODO: Pass exceptions to error log instead of crashing the app
                pass
        
        return render_template(Routes.Pages['Search'], result=response_data)
    
    @blueprint.route('/image', methods=['POST'])
    def process_image_route():
        response_data = None
        
        if request.method == 'POST':
            try:
                response_data = image_process_image_request(request)
            except:
                # TODO: Pass exceptions to error log instead of crashing the app
                pass
            
            return response_data, 200
        
        else:
            
            return 'Method Not Allowed', 405
    
    def process_search_request(request):
        search = Routes.api.endpoints.search
        
        # The api search endpoint params happen to be the same as these post params
        search.params.imdb_id           = request.form.get('imdb_id')
        search.params.movie_title_query = request.form.get('movie_title_query')
        search.params.result_type       = request.form.get('result_type')
        search.params.release_year      = request.form.get('release_year')
        search.params.plot_length       = request.form.get('plot_length')
        
        search_response = Routes.api.exec(search).getresponse()
        
        # TODO: Look into how expensive it is to pass whole responses like this.
        #       It would likely be much cheaper to do the work inline here instead
        return process_search_respose(search_response)
    
    def process_search_respose(search_response):
        pass #TODO
    
    def process_image_request(request):
        image = Routes.api.endpoints.image
        
        # The api image endpoint params happen to be the same as these post params
        image.params.imdb_id           = request.form.get('imdb_id')
        image.params.movie_title_query = request.form.get('movie_title_query')
        image.params.result_type       = request.form.get('result_type')
        image.params.release_year      = request.form.get('release_year')
        image.params.plot_length       = request.form.get('plot_length')
        
        image_response = api.exec(image).getresponse()
        
        # TODO: Look into how expensive it is to pass whole responses like this.
        #       It would likely be much cheaper to do the work inline here instead
        return process_image_respose(image_response)
    
    def process_image_respose(image_response):
        pass #TODO
