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
    CSRF_ENABLED = True

class ProductionConfig(Config):
    """
    Live environment with production data
    """
    pass

class StagingConfig(Config):
    """
    Pre-production environment with production data
    """
    pass

class DevelopmentConfig(Config):
    """
    Development environment with sample data for development.
    Can be hosted locally or deployed on a shared host environment
    """
    pass

class TestingConfig(Config):
    """
    Testing environment with mock test data for running tests
    """
    pass

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
