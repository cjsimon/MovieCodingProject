# TODO: Allow reserved keywords in the dict by making keys case-insensitive,
#       or make a flag to toggle case-insensitivity so that reserved keywords
#       can still work. For now, just using attr.Type instead of attr.type...

class attrs(dict):
    """
    Manage nested dicts using class instances,
    referencing key-values through class attribute paths
    """
    
    def __getattr__(self, name):
        """
        Get the value of a given attr key-pathname
        """
        
        keys = name.split('.')
        attr = self
        path = []
        
        # Traverse through the dict key-path getting the next dict value
        # until the final attr key-value from the key-path is retrieved
        for key in keys:
            if isinstance(attr, dict) and key in attr:
                attr = attr[key]
                path.append(key)
            else:
                class_name = getattr(self, '__name__', self.__class__.__name__)
                attr_path = '.'.join(path)
                
                raise AttributeError(f"'{class_name}.{attr_path}' has no attribute key '{key}'")
        
        return attr
    
    def __setattr__(self, name, value):
        """
        Set the value of a given attr key-pathname
        
        Any key that doesn't exist in attr key-path will be created
        """
        
        keys = name.split('.')
        attr = self
        
        for key in keys[:-1]:
            if key not in attr or not isinstance(attr[key], dict):
                attr[key] = __class__()
            
            attr = attr[key]
        
        attr[keys[-1]] = value
    
    def __delattr__(self, name):
        """
        Delete a given attr given its key-pathname
        """
        
        keys = name.split('.')
        attr = self
        path = []
        
        for key in keys[:-1]:
            if key in attr and isinstance(attr[key], dict):
                attr = attr[key]
                path.append(key)
            
            else:
                instance_name = getattr(self, '__name__', self.__class__.__name__)
                attr_path = '.'.join(path)
                
                raise AttributeError(f"'{instance_name}.{attr_path}' has no attribute key '{key}'")
        
        del attr[keys[-1]]
    
    def __iter__(self):
        return self.iterate()
    
    def iterate(self, parent_key='', depth=None, _current_depth=0):
        """
        The iterator implementation for traversing through
        nested dict keys down to a given certain depth
        """
        
        for attr_key, attr_value in self.items():
            full_key = f"{parent_key}.{attr_key}" if parent_key else attr_key
            
            if isinstance(attr_value, dict) and (depth is None or _current_depth < depth):
                yield from self.iterate(full_key, depth, _current_depth + 1)
            else:
                yield full_key, attr_value
    
    def find_key(self, attr_path, full_path=False):
        """
        Find the key-path of a given nested attr-path
        """
        
        def _find_key(dic, target, path=''):
            """
            Find the key-path of a given nested dictionary key
            """
            
            # Traverse through the given dic looking for the target key-path
            for key, value in dic.items():
                current_path = f"{path}.{key}" if path else key
                
                if value is target:
                    # Found the target key-path
                    return current_path
                
                elif isinstance(value, dict):
                    # Recurse into this dic looking for the key-path
                    result = _find_key(value, target, current_path)
                    
                    if result:
                        # Found the target key-path (in the recursive function)
                        return result
            
            return None
        
        key_path = _find_key(dic=self, target=attr_path)
        if key_path:
            return key_path if full_path is True else key_path.split('.')[-1]
        
        return None
    
    def get_key(self, attr_path, full_path=False):
        """
        Return the path of a given attr-path
        
        The attr-path is an instance attribute path.
        This function traverses the dict to look for
        the key that corresponds to that attr-path, if
        it exists, else None is returned.
        """
        
        return self.find_key(attr_path, full_path)
