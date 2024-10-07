def str2bool(s):
    s = str(s).lower()
    
    if    s == 'true':  return True
    elif  s == 'false': return False
    else:               raise  ValueError('String must either be true or false')
