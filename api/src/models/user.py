from libs.flask_app import Serializer
from sqlalchemy import Column, Integer, String
from sqlalchemy import PrimaryKeyConstraint

def init(Base):
    """
    Init the table with a late binding inherited Base
    """
    
    class User(Base):
        __tablename__ = 'User'
        
        id    = Column(Integer,     nullable=False)
        email = Column(String(120), nullable=False)
        name  = Column(String(120), nullable=False, unique=False)
        PrimaryKeyConstraint(id)
        
        def __init__(self, email=None, name=None):
            """
            Initialize this instance's columns with the input data.
            This allows for managing a given single user record
            """
            
            self.email = email
            self.name  = name
        
        def __repr__(self):
            return '<PK: %r\nEmail: %r>' % (self.id, self.email)
        
        def serialize(self):
            Serializer.serialize(self)
    
    return User
