# OMDb API

Up to date as of Sept 29th, 2024. Refer to latest usage docs here: `https://www.omdbapi.com/#usage`

## Endpoints

Send all data requests to:  
`http://www.omdbapi.com/?apikey=[yourkey]&`

Poster API requests:  
`http://img.omdbapi.com/?apikey=[yourkey]&`

*Note: Both endpoints share the same parameters*

### Parameters

#### By ID or Title

Parameter | Required | Valid Options | Default Value | Description
| - | - | - | - | - |
i | [Optional]* | | \<empty> | A valid IMDb ID (e.g. tt1285016)
t | [Optional]* | | \<empty> | Movie title to search for.
type | No | movie, series, episode | \<empty> | Type of result to return.
y | No | | \<empty> | Year of release.
plot | No | short, full | short | Return short or full plot.
r | No | json, xml | json | The data type to return.
callback | No | | \<empty> | JSONP callback name.
v | No | | 1 | API version (reserved for future use).

\**Please note while both "i" and "t" are optional at least one argument is required.*

#### By Search

Parameter | Required | Valid Options | Default Value | Description
| - | - | - | - | - |
s | Yes | | \<empty> | Movie title to search for.
type | No | movie, series, episode | \<empty> |	Type of result to return.
y | No | | \<empty> | Year of release.
r | No | json, xml | json | The data type to return.
page [New!] | No | 1-100 | 1 | Page number to return.
callback | No | | \<empty> | JSONP callback name.
v | No | | 1 | API version (reserved for future use).
