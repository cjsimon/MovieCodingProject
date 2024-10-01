from flask import Blueprint, render_template
import os

class Routes:
    
    """
    A static list of available pages within the webapp
    """
    Pages = None
    
    """
    The blueprint to be registered by the parent_app instance.
    
    These routes are for defining and handling web pages
    """
    blueprint = Blueprint('app', __name__)
    
    def __init__(self, parent_app):
        """ App Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.app = parent_app
        
        """ The pages directory relative to the webroot """
        self.pages_dir = os.path.join(self.app.config['BASEDIR'], 'pages')
        
        # Do not re-determine Pages if they've already been determined
        if self.Pages is None:
            # All pages are dict values with their page name as the key,
            # and the following path within the pages_dir: {page}/{page}.html
            self.Pages = { page: os.path.join(self.pages_dir, '%(page)s/%(page)s.html' % { 'page': page }) for page in [
                'Main'
            ]}
    
    @blueprint.route('/', methods = ['GET', 'POST'])
    def index():
        return render_template(Pages.Main)
