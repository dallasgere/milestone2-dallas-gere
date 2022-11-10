# project1-your-dallas-gere
### (https://movie-site.fly.dev "my movie app website!")

## my technologies, frameworks, api's
1. language
    * python was the only programming language that i used for my app
2. technologies
    * html - this was used to format my webpage
    * css - this was used to style my html and make things look better
    * flask - this is how i set up my web server
    * fly.io - this is what was used to deploy my app to the big internet
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
1. one thing that differed from how i thought it was going to work was adding comments to the movies. I didnt know how i 
## Detailed description of 2+ technical issues and how you solved them (your process, what you searched, what resources you used)
1. The biggest issue that i had with this project was making my flask login features work.  