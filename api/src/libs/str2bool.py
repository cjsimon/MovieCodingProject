def str2bool(s, fallback=None):
    if isinstance(s, bool):
        return s
    
    s = str(s).lower()
    
    if    s == 'true':          return True
    elif  s == 'false':         return False
    elif  fallback is not None: return fallback
    else:                       raise  ValueError('String must either be \'true\' or \'false\'')
