from sqlalchemy.inspection import inspect as sqlalchemy_inspect

class Serializer(object):
    """
    Serialize model instances for viewing and debugging
    """
    
    @staticmethod
    def serialize(self):
        """
        Return a dictionary of attirbutes of a given object instance
        """
        return { attr_key: getattr(self, attr) for attr_key in sqlalchemy_inspect(self).attrs.keys() }
    
    @staticmethod
    def serialize_list(lst):
        """
        Serialize each element of a list
        
        Note: The elements much be objects
        """
        return [ obj.serialize() for obj in lst ]
