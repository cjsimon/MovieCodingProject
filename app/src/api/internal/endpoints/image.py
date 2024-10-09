def endpoint():
    return {
        'route':  '/image',
        'method': 'POST',
        'params': {
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
            'page': {
                'desc':     'Page number to return.',
                'Type':     int,
                'options':  lambda i: 0 < i and i <= 100,
                'required': False,
                #'value':   #page
            },
        }
    }
