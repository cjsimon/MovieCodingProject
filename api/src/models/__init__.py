from sqlalchemy.ext.declarative import declarative_base

class Models():
    '''
    A container that manages and holds the list of models that make up the database
    '''
    
    '''
    Generate a Base type for the models to inherit in order for these
    classes to inherit the parent class that flask expects of models
    
    This Base class will be populated with a flask specified base before the models are initialized
    '''
    Base = None
    
    ''' The list of models that make up the tables of the database '''
    models = {}
    
    def __init__(self, Base):
        ''' Populate the Base class for the models with the passed in flask specified base '''
        self.Base = Base
    
    def init_models(self):
        '''
        Import and store a reference to the models
        '''
        
        # Import all models being used in the application here
        from .user         import init as User
        from .movie        import init as Movie
        from .users_movies import init as Users_Movies
        
        # Store a reference of each module
        # without instantiating, aka init()'ing, it
        self.models.update({
            'User':         User        (self.Base),
            'Movie':        Movie       (self.Base),
            'Users_Movies': Users_Movies(self.Base),
        })
        return self
    
    def get_module(self, model=None):
        '''
        Return a specified model from the list of models
        '''
        
        if model is None:
            pass
        
        return self.models[model]
