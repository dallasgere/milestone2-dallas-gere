# milestone2-your-dallas-gere
### (https://dallas-movies.fly.dev "my movie app website!")

## my technologies, frameworks, api's
1. language
    * python was the only programming language that i used for my app
2. technologies
    * html - this was used to format my webpage
    * css - this was used to style my html and make things look better
    * flask - this is how i set up my web server
    * fly.io - this is what was used to deploy my app to the big internet
    * black formatter - this is the tool we use to format our code better
3. libraries
    * os - this was used to get my api key from my .env file through my operating system
    * random - this is used to get a random movie from my list of top movies
    * requests - this was used to get a request from the api and format it in json
    * dotenv - this is used to get by api key from the .env file
    * flask-login - this is how i was able to implement the login features
    * SQLAlchemy - this made for an easy way to build the database models and to communicate with my database using python code
4. API's
    * tmdb api - this is where i retrieved all of my api data and you have to make a .env file to put your api key in
    * wikipedia api - this is where i got the link to my movie thats currently being displayed 

## how to run this program if you clone my repo
#### these are the steps listed as to how to run my code
1. you will need to download fly.io from the fly website on your terminal
  * this is done with brew install flyctl on mac
2. then you will need to run the flyctl launch command to make the fly.toml file and the procfile
    * dont edit the fly.toml file
    * in the Procfile change hellofly to server, server is the name of my file with the instance for app.run
3. make a file called requirements.txt in your project folder
    * in this file list all your dependencies that your python code is using
    * these should be
        1. click==8.1.3
        2. gunicorn==20.1.0
        3. itsdangerous==2.1.2
        4. Jinja2==3.1.2
        5. MarkupSafe==2.1.1
        6. Werkzeug==2.2.2
        7. requests==2.22.0
        8. python-dotenv==0.21.0
        9. Flask-SQLAlchemy==3.0.2
        10. greenlet==2.0.0
        11. importlib-metadata==5.0.0
        12. psycopg2-binary==2.9.5
        13. SQLAlchemy==1.4.42
        14. zipp==3.10.0
        15. flask-login==0.6.2

4. then everything should be set for you to deploy the app now
    * to deploy run flyctl deploy in your terminal
    * then it should do everything for you and work!

## Detailed description of 2+ examples where implementing your project differed from your expectations during project planning.
1. one thing that differed from how i thought it was going to work was adding a database to my project. I thought there was going to be a lot more invovled in this but there was not as much as i had initially anticipated. All i had to do was setup my flask sqlalchemy stuff correctly as well as make a database model, and then fly just did everything else for me. All i had to do was proxy to the database and then i was able to run locally. I was expecting the database part to be the most intensive part of this project but fly and sqlalchemy made it a lot easier than i thought it would be. I thought it was really cool how sql alchemy was able to talk to my database without me having to do sql queries
2. another thing that worked out differently than i thought was the black formatter. I heard a lot of other people having problems trying to get it set up and i thought it was going to be a big problem. But really i just was able to read the documentation on vscode and it worked really easily and i thought it was a really cool tool. I hate messy code and i love the fact that there is a formatter that will clean everything up for you
## Detailed description of 2+ technical issues and how you solved them (your process, what you searched, what resources you used)
1. The biggest issue that i had with this project was making my flask login features work. I had lots of trouble trying to get my user logged in, out, and using the login required decorator. I followed many youtube videos and all the online resources we were given and i just couldnt get it to work. The problem turned out to be that on my login i was making a new instance of my person class and trying to log that in instead of just logging in the user i was checking for. This was a problem because when i made the new user it was not committed to the database and i was just checking if a user who was never in the database was actually there. Also i had a problem with the flask login formatting stuff. 
    * these were app.config["TESTING"] = False
    * and @app.before_first_request
    def init_app():
    """
    making sure user is logged out just in case of cookies
    """
    logout_user()   
these made it so that my browser could not remember that the user was logged in through cookies and made it so that the user had to log in everytime. I was able to go to office hours and the professor and a classmate helped me debug and i was able to find the app config stuff on a stack overflow question and after that everything was working.
2. I was also having a lot of problems just trying to format my pages that displayed the movie information once i introduced the form that allowed users to input comments. I just copied my repo from the first project and built onto it and I think that my html and css from the first project couldve been done better as it was very messy and everything felt more like a blob rather than individual components. I would have made it more modular because in this version if i moved one component then everything would get jumbled up. Eventually through some trial and error and looking for answers on w3 schools and stackoverflow i was able to put all the components together how i wanted them to be and learned more about css and html elements.