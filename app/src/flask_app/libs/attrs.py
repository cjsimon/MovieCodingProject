# TODO: Allow reserved keywords in the dict by making keys case-insensitive,
#       or make a flag to toggle case-insensitivity so that reserved keywords
#       can still work. For now, just using attr.Type instead of attr.type...

class attrs(dict):
    def __getattr__(self, name):
        keys = name.split('.')
        value = self
        path = []
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
                path.append(key)
            else:
                object_name = getattr(self, '__name__', self.__class__.__name__)
                attr_path = '.'.join(path)
                
                raise AttributeError(f"'{object_name}.{attr_path}' has no attribute key '{key}'")
        
        return value
    
    def __setattr__(self, name, value):
        keys = name.split('.')
        attr = self
        
        for key in keys[:-1]:
            if key not in attr or not isinstance(attr[key], dict):
                attr[key] = __class__()
            
            attr = attr[key]
        
        attr[keys[-1]] = value
    
    def __delattr__(self, name):
        keys = name.split('.')
        attr = self
        path = []
        
        for key in keys[:-1]:
            if key in attr and isinstance(attr[key], dict):
                attr = attr[key]
                path.append(key)
            
            else:
                object_name = getattr(self, '__name__', self.__class__.__name__)
                attr_path = '.'.join(path)
                
                raise AttributeError(f"'{object_name}.{attr_path}' has no attribute key '{key}'")
        
        del attr[keys[-1]]
    
    def __iter__(self):
        return self.iterate()
    
    def iterate(self, parent_key='', depth=None, _current_depth=0):
        for attr_key, attr_value in self.items():
            full_key = f"{parent_key}.{attr_key}" if parent_key else attr_key
            
            if isinstance(attr_value, dict) and (depth is None or _current_depth < depth):
                yield from self.iterate(full_key, depth, _current_depth + 1)
            else:
                yield full_key, attr_value
    
    def find_key(self, ref, full_path=False):
        def _find_key(d, target, path=''):
            for k, v in d.items():
                current_path = f"{path}.{k}" if path else k
                if v is target:
                    return current_path
                elif isinstance(v, dict):
                    result = _find_key(v, target, current_path)
                    if result:
                        return result
            return None
        
        key_path = _find_key(self, ref)
        if key_path:
            return key_path if full_path else key_path.split('.')[-1]
        return None
    
    def get_key(self, ref, full_path=False):
        return self.find_key(ref, full_path)
