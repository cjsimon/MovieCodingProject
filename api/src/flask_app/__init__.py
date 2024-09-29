from flask import Flask
from .configuration import get_environment_config
from .database import Database

class App:
    """
    A flask wrapper for instantiating Flask App instances
    """
    def __init__(self, env, use_database=False, create_tables):
        """
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
        from .routes import routes
        routes = Routes(db)
        app.register_blueprint(routes.app)
        
        return app
