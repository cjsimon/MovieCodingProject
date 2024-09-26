from flask import Flask
from .configuration import get_environment_config

class App:
    """
    A flask wrapper for instantiating Flask App instances
    """
    def __init__(self, env):
        """
        Create a flask instance with a specified config
        """
        app = Flask(__name__)
        
        # Given a valid Environment, attempt to instantiate,
        # then load-in, the corresponding Flask Config settings
        env_config = get_environment_config(env)
        app.config.from_object(env_config)
        
        # Register the flask_app's routes and bind them to the app
        from .routes import routes
        app.register_blueprint(routes.app)
        
        return app
