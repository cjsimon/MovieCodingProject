from flask import Blueprint, render_template

class Routes:
    
    """
    A static list of available pages within the webapp
    """
    Pages = None
    
    def __init__(self, parent_app) {
        """ Routes constructor """
        
        """ The parent app instance this Routes instance belongs to """
        self.parent_app = app
        
        """ The app blueprint for defining and handling routes """
        self.app_blueprint = Blueprint('app', __name__)
        
        """ The pages directory relative to the webroot """
        self.pages_dir = os.path.join(app.instance_path, 'pages')
        
        """
        All pages are dict values with their page name as the key,
        and the following path within the pages_dir: {page}/{page}.html
        """
        Pages = { page: os.path.join(pages_dir, '%s/%s.html' % page) for page in [
            'Main'
        ]} if Pages is None else Pages # Do not re-determine Pages if they've already been determined
    }
    
    @app_blueprint.route('/', methods = ['GET', 'POST'])
    def index():
        return render_template(Pages.Main)
