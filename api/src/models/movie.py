from flask_app.serializer import Serializer
from sqlalchemy import Column, Integer, String
from sqlalchemy import PrimaryKeyConstraint

def init(Base):
    """
    Init the table with a late binding inherited Base
    """
    
    class Movie(Base):
        __tablename__ = 'Movie'
        
        id       = Column(Integer,     nullable=False)
        title    = Column(String(120), nullable=False, unique=False)
        year     = Column(String,      nullable=True,  unique=False) # Using String as workaround; the year shouldn't auto-increment.
                                                                    # See: https://github.com/sqlalchemy/sqlalchemy/discussions/10921
                                                                    # As a positive, the year could now support parenthesis and extras.
        rating   = Column(Integer,     nullable=True,  unique=False)
        plot     = Column(String(120), nullable=True,  unique=False)
        director = Column(String(120), nullable=True,  unique=False)
        actors   = Column(String(120), nullable=True,  unique=False) # TODO: Construct actors on the fly with db table?
                                                                    #       Could also do this for the Movies as well
        PrimaryKeyConstraint(id)
        PrimaryKeyConstraint(title)
        PrimaryKeyConstraint(year)
        
        def __init__(self, title=None, year=None, rating=None, plot=None, director=None, actors=None):
            """
            Initialize this instance's columns with the input data.
            This allows for managing a given single movie record
            """
            
            self.title    = title
            self.year     = year
            self.rating   = rating
            self.plot     = plot
            self.director = director
            self.actors   = actors
        
        def __repr__(self):
            return '<Id: %r\nTitle: %r\nYear: %r>' % (self.id, self.title, self.year)
        
        def serialize(self):
            Serializer.serialize(self)
    
    return Movie
