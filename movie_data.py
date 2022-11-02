'''
This file is where we will use our api's to retrieve data about movies
'''
#import json
import os
import random
import requests
from dotenv import load_dotenv
load_dotenv()

class MovieData:
    '''
    this is the class that will contain all the functions to retrieve information about movie data
    '''
    @staticmethod
    def searching_for_movie(movie_name):
        '''
        this method will give me the top movies!!
        '''

        tmdb_api_key = os.getenv("tmdb_api_key")
        base_url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={movie_name}"
        response = requests.get(
            base_url,
            params = {
                "api_key": tmdb_api_key
            }
        )

        movie_json_data = response.json()
        #pretty_json_data = json.dumps(movie_json_data, indent = 1, sort_keys=True)
        movie_id = movie_json_data['results'][0]['id']
        #print(article_object)
        #print(pretty_json_data)

        return movie_id

    @staticmethod
    def movie_image_search(movie_id):
        '''
        this function will search for and return the movie image
        '''

        tmdb_api_key = os.getenv("tmdb_api_key")
        base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={tmdb_api_key}"
        response = requests.get(
            base_url,
            params = {
                "movie_id": movie_id
            }
        )

        movie_image = response.json()
        #pretty_json_data = json.dumps(movie_image, indent = 1, sort_keys=True)
        #print(pretty_json_data)
        image_path = movie_image['backdrops'][0]['file_path']
        #print(image_path)
        image_link = f"https://image.tmdb.org/t/p/w500{image_path}"
        return image_link

    @staticmethod
    def get_movie_genre(movie_id):
        '''
        this function will return the genre of a movie when provided with an movie id
        '''

        tmdb_api_key = os.getenv("tmdb_api_key")
        base_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}"
        response = requests.get(
            base_url,
            params = {
                "movie_id": movie_id
            }
        )

        result = response.json()
        movie_genre = result['genres'][0]['name']

        return movie_genre

    @staticmethod
    def get_movie_tagline(movie_id):
        '''
        this function will retrieve the movie tagline with an api, however i should probably make this all one function
        '''

        tmdb_api_key = os.getenv("tmdb_api_key")
        base_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}"
        response = requests.get(
            base_url,
            params = {
                "movie_id": movie_id
            }
        )

        result = response.json()
        movie_tagline = result['tagline']

        return movie_tagline


    @staticmethod
    def random_top_movies():
        '''
        This function will give me all the information to get random top movies
        '''

        top_ten_movies_list = []
        tmdb_api_key = os.getenv("tmdb_api_key")
        article_path = "/trending/movie/week?"
        base_url = f"https://api.themoviedb.org/3{article_path}"

        response = requests.get(
            base_url,
            params = {
                "api_key": tmdb_api_key
            }
        )

        json_data = response.json()
        for i in range(10):
            top_ten_movies_list.append(json_data['results'][i]['title'])

        return random.choice(top_ten_movies_list)

    @staticmethod 
    def wiki_api(movie_title):
        '''
        this function will return a link to my wiki api
        '''

        url = "https://en.wikipedia.org/w/api.php"
        title = movie_title + " film"

        parameters = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "info",
            "inprop": "url|talkid",
        }

        response = requests.get(
            url,
            parameters
        )

        json_data = response.json()
        link = json_data['query']['pages']['-1']['fullurl']

        return link
