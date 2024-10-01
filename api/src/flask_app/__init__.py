from flask import Flask
from .configuration import get_environment_config
from .database import Database

def create_app(env):
    """
    A Flask app factory.
    Create a flask instance with a specified config
    """
        
    app = Flask(__name__)
    
    # Given a valid Environment, attempt to instantiate,
    # then load-in, the corresponding Flask Config settings
    env_config = get_environment_config(env)
    app.config.from_object(env_config)
    
    if use_database:
        # Create a db instance with a scoped session and base.
        # Bind it to the app, and create table schema if requested
        db = Database(app, create_tables)
    
    # Register the flask_app's routes, then bind them to the app
    import routes
    routes = Routes(app, db)
    app.register_blueprint(routes.blueprint)
    
    return app
