from flask_app.configuration import Config
from flask import Blueprint, render_template
import os

"""
The pages directory relative to the webroot

TODO: Blueprint routes don't easily accept self references.
      Just use the static Config.BASEDIR for now instead
      of the one from the parent app instance
"""
pages_dir = os.path.join(Config.BASEDIR, 'pages/')

class Routes:
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling web pages
    """
    blueprint = Blueprint('app', __name__)
    
    """
    A static list of available pages within the webapp
    
    TODO: Move to App instead of defining here in routes?
    """
    Pages = { page: '%(page)s/%(page)s.html' % { 'page': page } for page in [
        'Main'
    ]}
    
    def __init__(self, parent_app, parent_database=None):
        """ App Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The parent database instance this Routes instance belongs to """
        self.database = parent_database
    
    @blueprint.route('/', methods = ['GET', 'POST'])
    def index():
        return render_template(Routes.Pages['Main'])
