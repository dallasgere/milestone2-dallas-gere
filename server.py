'''
this file is where i will define all my routes for my website and run the app
'''
import os
import flask
from flask import request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
#from flask_bcrypt import Bcrypt
import movie_data
import requests
load_dotenv()

app = flask.Flask(__name__)
app.secret_key = 'secret'
#bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
app.config['TESTING'] = False

@app.before_first_request
def init_app():
    '''
    making sure user is logged out just in case of cookies
    '''
    logout_user()

# the login stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_form'

# all the database stuff
class Comment(db.Model):
    '''
    this is the model of my comment database
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        '''
        returns the stuff
        '''
        return '<User %r>' % self.comment

#class Person(UserMixin, db.Model):
class Person(UserMixin, db.Model):
    '''
    this is the model of my users database
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    #comment = db.relationship('Comment', backref='person')

    #def get_id(self):
        #"""Return the email address to satisfy Flask-Login's requirements."""
       # return id

    def __repr__(self):
        '''
        idk just good to have
        '''
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    '''
    returns the object of the user id turned in
    '''

    return Person.query.get(int(user_id))
    #return Person.get_id(user_id)
    #pass
    #return Person.query.filter_by(user_id).first()
    #return Person(username=user_id)
    #return Person.get_id((user_id))
    #return Person.query.get(int(id))

# these are all my routes
@app.route('/test')
def test():
    '''
    just a function for testing
    '''

    return [str(person) for person in Person.query.all()]

@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    '''
    this is the function that logs out my user
    '''
    user = current_user.username
    logout_user()
    return flask.render_template('logout.html', user=user)

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
    name = form_data['username']
    if_user_exist = Person.query.filter_by(username=name).first()
    if if_user_exist is None:
        new_person = Person(username=name)
        db.session.add(new_person)
        db.session.commit()

        # trying some login stuff
        login_user(new_person)

        return flask.redirect(flask.url_for('home'))
    else:
        flask.flash('account already exist, please login')
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
    name = login_form_data['username']
    if_user_exist = Person.query.filter_by(username=name).first()

    # logging the person in if authenticated
    if if_user_exist is not None:
        login_user(if_user_exist)
        return flask.redirect(flask.url_for('home'))
    else:
        flask.flash('you fool!! username does not exist')
        return flask.redirect(flask.url_for('login_form'))

@app.route('/comment_form', methods=['POST', 'GET'])
def comment_form():
    '''
    this is the form that will allow users to add comments
    '''

    return flask.render_template('comment_form.html')

@app.route('/comment_handler', methods={'POST', 'GET'})
def comment_handler():
    '''
    this will handle the comment information
    '''

    comment_form_data= flask.request.form
    comment = comment_form_data['comment']
    movie_name = comment_form_data['movie_name']
    rating = comment_form_data['rating']
    movie_id = movie_data.MovieData.searching_for_movie(movie_name)
    new_comment = Comment(username=current_user.username, movie_id=movie_id, comment=comment, rating=rating)
    db.session.add(new_comment)
    db.session.commit()

    return flask.render_template('comment_handler.html', comment=comment)

@app.route("/search_movie_form", methods=['POST', 'GET'])
@login_required
def search_movie_form():
    '''
    this is the function that allows users to search for movies and redirect to page to display the data
    '''

    return flask.render_template('search_movie_form.html')

@app.route("/search_movie_display", methods=['POST', 'GET'])
@login_required
def search_movie_display():
    '''
    this function will check if the value entered is a okay input and then display the movie data
    '''

    search_movie_form_data = flask.request.form
    movie_name = search_movie_form_data['movie_name']

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

    comments = []
    users = []
    ratings = []
    for i in Comment.query.filter_by(movie_id=str(movie_id)):
        comments.append(i.comment)
        users.append(i.username)
        ratings.append(i.rating)

    size = len(comments)

    return flask.render_template(
        "search_movie_display.html",
        title = movie_dict["title"],
        tagline = movie_dict["tagline"],
        genre = movie_dict["genre"],
        poster = movie_dict["poster"],
        link = movie_dict["link"],
        comments = comments,
        users = users,
        ratings = ratings,
        size = size
    )

@app.route("/home", methods=['POST', 'GET'])
@login_required
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
