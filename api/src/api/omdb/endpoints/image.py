def endpoint():
    return {
        'host':   'http://www.img.omdbapi.com',
        'route':  '/',
        'method': 'GET',
        'params': {
            'apikey': {
                'desc':     'API key.',
                'Type':     str,
                'required': True,
                #'value':   os.environ.get('APPLICATION_OMDBAPI_KEY'),
            },
            's': {
                'desc':     'Movie title to search for.',
                'Type':     str,
                'required': True,
                #'value':   movie_title_query,
            },
            'Type': {
                'desc':     'Type of result to return.',
                'Type':     str,
                'options':  ['movie', 'series', 'episode'],
                'required': False,
                #'value':   result_type,
            },
            'y': {
                'desc':     'Year of release.',
                'Type':     int,
                'required': False,
                #'value':   #release_year,
            },
            'r': {
                'desc':     'The data type to return.',
                'Type':     str,
                'options':  ['json', 'xml'],
                'required': False,
                'value':    'json',
            },
            'page': {
                'desc':     'Page number to return.',
                'Type':     int,
                'options':  lambda i: 0 < i and i <= 100,
                'required': False,
                #'value':   #page
            },
            'callback': {
                'desc':     'JSONP callback name.',
                'Type':     str,
                'value':    None,
                'required': False,
            },
            'v': {
                'desc':     'API version (reserved for future use).',
                'Type':     str,
                'required': False,
                'value':    None,
            },
        }
    }
