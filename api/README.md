# Movie Manager WebAPI

The Movie Manager API for, currently, just the WebApp to interface with. Currently, the WebAPI is just a wrapper for the [OMDb API](https://www.omdbapi.com/), and a bridge for the [Movie Manager WebApp](../app/README.md) to interface with the [Movie Manager Database](../database/).

## OMDb API

This API makes use of the [OMDb API](https://www.omdbapi.com/) internally. See the official documentation [here](https://www.omdbapi.com#parameters), and the manually-mirrored local doc ingestion [here](./OMDb%20API.md), under `./OMDb API.md`

## Internal Endpoints

### Get Movies

Route Endpoint: `/movies/search`  
Method: POST  

***TODO***

#### Get a Movie's Image

Route Endpoint: `/movie/image`  
Method: POST  

***TODO***

#### Get a User's Favorite Movies

Route Endpoint: `/<user_id>/movies/favories`  
Method: POST  

***TODO***

#### Save a User's Favorite Movies

Route Endpoint: `/<user_id>/movies/save`  
Method: POST  

***TODO***
