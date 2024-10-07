import os, sys

from enum import StrEnum

class Environment(StrEnum):
    """
    The types of app environments
    """
    
    PRODUCTION  = 'PRODUCTION'
    STAGING     = 'STAGING'
    DEVELOPMENT = 'DEVELOPMENT'
    TESTING     = 'TESTING'

class Config(object):
    """
    Configuration base for all app environments
    """
    
    #TODO: Don't hardcode path traversal for BASE_PATH
    BASE_PATH    = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    CSRF_ENABLED = True
    
    # dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = \
        'mariadb+mariadbconnector://%(username)s:%(password)s@%(hostname)s:%(hostport)s/%(database)s' % {
            'username': os.environ.get('DATABASE_USER'),
            'password': os.environ.get('DATABASE_PASS'),
            'hostname': os.environ.get('DATABASE_HOST'),
            'hostport': os.environ.get('DATABASE_PORT'),
            'database': os.environ.get('DATABASE_NAME'),
        }
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    TEMPLATE_DIR  = 'pages'
    TEMPLATE_PATH = os.path.join(BASE_PATH, TEMPLATE_DIR)
    
class ProductionConfig(Config):
    """
    Live environment with production data
    """
    
    SECRET_KEY = 'E?MF@p,dG^2?t|d<'

class StagingConfig(Config):
    """
    Pre-production environment with production data
    """
    
    SECRET_KEY = '/sgbLm3DA#>)+ZQ{'

class DevelopmentConfig(Config):
    """
    Development environment with sample data for development.
    Can be hosted locally or deployed on a shared host environment
    """
    
    SECRET_KEY = '78B_B?rY&x(u52n*'
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """
    Testing environment with mock test data for running tests
    """
    
    SECRET_KEY = '4th&$Y9De{U/X$>A'
    SQLALCHEMY_ECHO = True

def get_environment_config(env):
    """
    Return a new Environment instance given an Environment enum
    
    Note: This is only meant to utilized once per app instantiation
    """
    
    env_selection = {
        Environment.PRODUCTION:  ProductionConfig(),
        Environment.STAGING:     StagingConfig(),
        Environment.DEVELOPMENT: DevelopmentConfig(),
        Environment.TESTING:     TestingConfig()
    }
    selected_env = env_selection.get(env)
    
    if selected_env is None:
        sys.exit(
            'Environment error: %s is not a valid configuration!\nPossible values are %s'
            % (env, [(env.value) for env in Environment]))
    else:
        return selected_env
