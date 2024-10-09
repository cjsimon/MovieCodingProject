from flask import Flask
from flask_cors import CORS

from .configuration    import Environment, get_environment_config
from .database         import Database
from .model_serializer import Serializer

def create_app(name, env, use_database, create_tables):
    """
    A Flask app factory.
    Create a flask instance with a specified config
    
    # TODO: Wrap flask app insances with a class so you can pass for example,
            the Config and Routes instances alongside the flask app instance
    """
    
    app = Flask(name if name is not None else __name__)
    
    # Disable CORS for js modules that,
    # unlike other resources for some reason,
    # aren't working with it enabled.
    #
    # There might be a better way to get CORS
    # working with js modules
    #
    CORS(app, resources={
        r'/static/libraries/*': {
            'origins': '*'
        }
    })
    
    # Given a valid Environment, attempt to instantiate,
    # then load-in, the corresponding Flask Config settings
    env_config = get_environment_config(env)
    app.config.from_object(env_config)
    
    # Set server paths
    app.template_folder=env_config.TEMPLATE_PATH
    app.static_folder=env_config.STATIC_PATH
    
    # Create a db instance with a scoped session and base.
    # Bind it to the app, and create table schema if requested
    db = Database(app, create_tables) if use_database is True else None
    
    # Register the flask_app's routes, then bind them to the app
    from routes import Routes
    routes = Routes(app, db)
    app.register_blueprint(routes.blueprint)
    
    return app
