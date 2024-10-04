from flask import Flask

from .configuration import Environment, get_environment_config
from .database      import Database

def create_app(name, env, use_database, create_tables):
    """
    A Flask app factory.
    Create a flask instance with a specified config
    """
    
    app = Flask(name if name is not None else __name__)
    
    # Given a valid Environment, attempt to instantiate,
    # then load-in, the corresponding Flask Config settings
    env_config = get_environment_config(env)
    app.config.from_object(env_config)
    
    app.template_folder=env_config.TEMPLATE_FOLDER
    
    # Create a db instance with a scoped session and base.
    # Bind it to the app, and create table schema if requested
    db = Database(app, create_tables) if use_database else None
    
    # Register the flask_app's routes, then bind them to the app
    from routes import Routes
    routes = Routes(app, db)
    app.register_blueprint(routes.blueprint)
    
    return app
