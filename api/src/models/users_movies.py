from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
from api.serializer import Serializer

def init(Base):
    """
    Init the table with a late binding inherited Base
    """
    
    class Users_Movies(Base):
        __tablename__ = 'Users_Movies'
        
        user_id  = Column(Integer)
        movie_id = Column(Integer)
        PrimaryKeyConstraint(
            'user_id'
            'movie_id',
            name='pk_user_movie'
        ),
        ForeignKeyConstraint(['user_id', 'User.id'], name='fk_user'
            onupdate='RESTRICT',
            ondelete='CASCADE'
        )
        ForeignKeyConstraint(['movie_id', 'Movie.id'], name='fk_movie'
            onupdate='RESTRICT',
            ondelete='CASCADE'
        )
        
        def __init__(self, user_id=None, movie_id=None):
            """
            Initialize this instance's columns with the input data.
            This allows for inserting a single user into the database
            """
            
            self.user_id  = user_id
            self.movie_id = movie_id
            
        def serialize(self):
            Serializer.serialize(self)
    
    return Users_Movies
