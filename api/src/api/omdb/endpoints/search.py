def endpoint():
    return {
        'url':    'http://www.omdbapi.com',
        'route':  '/',
        'method': 'GET',
        'params': {
            'apikey': {
                'desc':     'The api key to use.',
                'Type':     str,
                'required': True,
                #'value':   os.environ.get('APPLICATION_OMDBAPI_KEY'),
            },
            'i': {
                'desc':     'A valid IMDb ID (e.g. tt1285016)',
                'Type':     int,
                'required': False,
                #'value':   imdb_id,
            },
            't': {
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
                #'value':   release_year,
            },
            'plot': {
                'desc':     'Return short or full plot.',
                'Type':     str,
                'options':  ['short', 'full'],
                'required': False,
                #'value':   plot_length
            },
            'r': {
                'desc':     'The data type to return.',
                'Type':     str,
                'required': False,
                'options':  ['json', 'xml'],
                'value':    'json',
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
