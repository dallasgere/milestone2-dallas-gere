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
        2. Flask==2.2.2
        3. gunicorn==20.1.0
        4. itsdangerous==2.1.2
        5. Jinja2==3.1.2
        6. MarkupSafe==2.1.1
        7. Werkzeug==2.2.2
        8. requests==2.22.0
        9. python-dotenv==0.21.0
4. then everything should be set for you to deploy the app now
    * to deploy run flyctl deploy in your terminal
    * then it should do everything for you and work!

## problems with my code i would fix with more time/features i would add with more time
1. my wikipedia link is off
    * so for the home page i call the top ten movies of the week and everytime you refresh the page it calls from the top ten movies of the week. A problem with this is that movie titles arent always unique. An example of this is the movie "Bullet Train" this is a movie name but there is also a wiki link for a bullet trains which are actual things in the world. So to try and solve this at the end of the movie title i add the word "film" and then call the wiki api link for that. This doesnt exactly work because there is no wikipedia page for a title called "Bullet Train Film". So instead the wikipedia link leads you to a page that suggests you go to the movie page instead of taking you directly there
2. i want to add a search feature
    * i wanted to add a button on top of my website that allowed users to search for movies and actors and what not, however i wasnt able to add this feature due to me not knowing how to use redirects at the time that i wanted to add it. After i learned redirects in flask i didnt have enough time to add this feature but it is one that i think will add a lot more functionality to my website

## technical issues
1. one technical issue that i had was that i could not figure out how to deploy to fly. I knew the fly launch and fly deploy commands and the fact that i had to set the secrets, but i did not know that i had to adjust my Procfile and that i had to make the requirements text file. So i just googled the error that fly was giving me and went down quite a long path trying to find the solution. I tried reading the fly suggested fixes and reading the forums on fly.io but nothing was working and every problem someone had online was very case specific and didnt align with what i was trying to fix. So after a long time reading different forums, watching videos, and making changes here and there, i asked a classmate for help and they were able to help me figure out what i didnt do and where to go from there. I didnt change my procfile and i didnt have the requirements text file set up correctly. The classmate reminded me that there is a demo on github that we used in class and i looked at that demo and that helped me a lot and i was eventually ready to deploy everything to fly and it worked!
2. Another technical issue that i had was that i had three python files
    * the first is called server and it defined my routes and talks to my html file and every function was in a class
    * the second is called movie_data and it calls all the api's and then returns the information back to my server file and everything is in a class
    * the third was called main and main is what i used to call the server file and in my main function i ran app.run
    * the fact that i didnt do app.run in my server.py file caused problems and fly could not find a file that had the words app.run because my files were so split up. this was fixed by getting rid of my main.py file and everything in my server file that was in class had to be taken out of the class and i put app.run and my main function at the bottom of my server file. This made everything work better on fly and i was eventually able to deploy the app.
    * this was a problem that i was able to figure out on my own and it just took a little thinking and reading the fly.io errors where it said app.run is not found in main. I was just able to figure out that it was probably because my files were split up so much and i made them not so split up and everything worked:)