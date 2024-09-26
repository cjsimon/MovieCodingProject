from flask import Blueprint, render_template

class Routes:
    app = Blueprint('app', __name__)
    
    # Get the pages directory relative to the webrpot
    pages_dir = os.path.join(app.instance_path, 'pages')
    
    # All pages are dict values with their page name as the key,
    # and the following path within the pages_dir: {page}/{page}.html
    Pages = { page: os.path.join(pages_dir, '%s/%s.html' % page) for page in [
        'Main'
    ]}
    
    @app.route('/', methods = ['GET', 'POST'])
    def index():
        return render_template(Pages.Main)
