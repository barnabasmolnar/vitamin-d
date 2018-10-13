# Get some vitamin D

This application lets you input a city into a form. Upon submission, you will receive a weather forecast ([from the Opeanweathermap API](https://openweathermap.org/api)) which shows the sunny periods the city will have up to 5 days. Why not plan a nice walk for one of these sunny periods to get some much needed vitamin D?

### Technologies used:
* Python
* Flask
* Server side rendering with Jinja templates
* Docker for development and to containerize the app

### A note about date/time:
The app displays date and time that is local to the queried city.
In order to achieve this functionality, the pendulum and timezonefinder python packages were used.

### SVGs used:
* [Zondicons - A set of free premium SVG icons. By Steve Schoger](http://www.zondicons.com/)

### Instructions to install and run this app locally:
* Clone the repo
* Create the credentials.py file in the app folder
* In it, include your openweathermap API key in the API_KEY variable, and a random string in the SECRET_KEY variable (as required by the Flask WTF-Forms package, see more here: https://flask-wtf.readthedocs.io/en/stable/csrf.html)
* Make sure Docker is installed
* Run docker-compose up -d
* Enjoy the sun!