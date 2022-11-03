'''
this file is where i will define all my routes for my website and run the app
'''
from crypt import methods
import flask
from flask import request
import movie_data

app = flask.Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def first():
    '''
    this is the page users will be prompted with and from this they will be able to login to the webpage
    '''
    return flask.render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
    '''
    the signup page
    '''

    form_data = flask.request.form
    username = form_data['username']
    if username == 'tay':
        return flask.redirect(flask.url_for('home'))
    else:
        flask.flash('username not found')
        return flask.redirect(flask.url_for('first'))

@app.route("/login_form", methods=['POST', 'GET'])
def login_form():
    '''
    this is the function that will display the login form
    '''

    return flask.render_template('login.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    '''
    this is the function that will prompt the user to login to the page
    '''

    login_form_data = flask.request.form
    username = login_form_data['username']
    if username == 'tay':
        return flask.redirect(flask.url_for('home'))
    else:
        return flask.redirect(flask.url_for('login_form'))

@app.route("/search_movie_form", methods=['POST', 'GET'])
def search_movie_form():
    '''
    this is the function that allows users to search for movies and redirect to page to display the data
    '''

    return flask.render_template('search_movie_form.html')

@app.route("/search_movie_display", methods=['POST', 'GET'])
def search_movie_display():
    '''
    this function will check if the value entered is a okay input and then display the movie data
    '''

    search_movie_form_data = flask.request.form
    movie_name = search_movie_form_data['movie_name']

    #if movie_name == 'movie':

    movie_title = movie_name
    movie_id = movie_data.MovieData.searching_for_movie(movie_title)
    movie_poster = movie_data.MovieData.movie_image_search(movie_id)
    movie_tagline = movie_data.MovieData.get_movie_tagline(movie_id)
    movie_genre = movie_data.MovieData.get_movie_genre(movie_id)
    wiki_link = movie_data.MovieData.wiki_api(movie_title)

    movie_dict = {
        "title": movie_title,
        "tagline": movie_tagline,
        "genre": movie_genre,
        "poster": movie_poster,
        "link": wiki_link
    }

    return flask.render_template(
        "search_movie_display.html",
        title = movie_dict["title"],
        tagline = movie_dict["tagline"],
        genre = movie_dict["genre"],
        poster = movie_dict["poster"],
        link = movie_dict["link"]
    )
    #else:
        #return flask.redirect(flask.url_for('search_movie_form'))

@app.route("/home", methods=['POST', 'GET'])
def home():
    '''
    this function will define my home page and will be part 1 for this project
    '''

    # initializing all the variables that im going to pass into my flask server
    movie_title = movie_data.MovieData.random_top_movies()
    movie_id = movie_data.MovieData.searching_for_movie(movie_title)
    movie_poster = movie_data.MovieData.movie_image_search(movie_id)
    movie_tagline = movie_data.MovieData.get_movie_tagline(movie_id)
    movie_genre = movie_data.MovieData.get_movie_genre(movie_id)
    wiki_link = movie_data.MovieData.wiki_api(movie_title)

    movie_dict = {
        "title": movie_title,
        "tagline": movie_tagline,
        "genre": movie_genre,
        "poster": movie_poster,
        "link": wiki_link
    }
    return flask.render_template(
        "index.html",
        title = movie_dict["title"],
        tagline = movie_dict["tagline"],
        genre = movie_dict["genre"],
        poster = movie_dict["poster"],
        link = movie_dict["link"]
    )

if __name__ == '__main__':
    app.run(debug=True)
