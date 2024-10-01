import sys
from enum import Enum

class Environment(Enum):
    """
    The types of app environments
    """
    PRODUCTION  = 'PRODUCTION'
    STAGING     = 'STAGING'
    DEVELOPMENT = 'DEVELOPMENT'
    TESTING     = 'TESTING'
    
    def __str__(self):
        return self.name

class Config(object):
    """
    Configuration base for all app environments
    """
    BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = \
        # dialect+driver://username:password@host/:port/database
        'mysql+mysqlconnector://%(username)s:%(password)s@%(hostname)s/:%(hostport)/%(database)s' % {
            username: args.dbuser
            password: args.dbpass
            hostname: args.dbhost
            hostport: args.dbport
            database: args.dbname
        }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
