from libs.flask_app import Serializer
from sqlalchemy import Column, Integer
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint

def init(Base):
    """
    Init the table with a late binding inherited Base
    """
    
    class Users_Movies(Base):
        __tablename__ = 'Users_Movies'
        
        user_id  = Column(Integer, nullable=False)
        movie_id = Column(Integer, nullable=False)
        PrimaryKeyConstraint(user_id, movie_id, name='pk_user_movie'),
        ForeignKeyConstraint(columns=['user_id'], refcolumns=['User.id'], name='fk_user',
            onupdate='RESTRICT',
            ondelete='CASCADE'
        )
        ForeignKeyConstraint(columns=['movie_id'], refcolumns=['Movie.id'], name='fk_movie',
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
