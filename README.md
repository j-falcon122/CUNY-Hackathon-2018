# SleepEZ

In a city that houses 63,343 homeless people in the municipal shelter system, we need to come up with improved ways of sharing information on available spaces for the needy to sleep during the night, especially those with no direct access to the internet. So how do the homeless, a user base that more likely than not can’t afford a cell phone with internet capabilities, find a shelter to stay the night in? They find it, with SleepEZ.


SleepEZ, designed to help those without access to the internet, is an app found on the ever emerging LinkNYC kiosks found around NYC. The app is created to fetch a users location and point them to the nearest shelter location in their area. The kiosks would also show the number of available beds within a 3 mile radius in a advertisement style ad, like the ones the LinkNYC kiosks already show users. 


We created this app in the hopes that we could help more of the homeless have a goodnights sleep.

## Built With 

Technologies used in the process of creating the app include HTML, CSS, Python, Django, Google Maps API, Bootstrap, Photoshop, and Illustrator.

## Try it out yourself
First, make sure you alread have installed Python, v 2.7 preferably, and Git.

To run, clone or [download](https://github.com/j-falcon122/CUNY-Hackathon-2018/archive/master.zip) the repository:

`git clone https://github.com/j-falcon122/CUNY-Hackathon-2018.git`

`cd CUNY-Hackathon-2018/Hackathon2018`

Install the required dependencies

`pip install -r requirements.txt`


Now, for the user settings, create a `.env ` file with the following:

```
 DEBUG_STATE = True
 SECRET_KEY = 'YOUR_SECRET_KEY'
 MAPS_API_KEY = 'YOUR_MAPS_API'
 EXTERNAL_DB = False
 ```
(For your Django secret key, you can [get one here](https://www.miniwebtool.com/django-secret-key-generator/) , For the  Google Maps API Key. You can [request it here](https://developers.google.com/maps/documentation/javascript/get-api-key) (Remember to enable it))
 
 ### External Database
 Depending on whether you want to use SQLite3, or MySQL, you may change the value of `EXTERNAL_DB` to True or False. If True, you need to add additional variables to your env file:
 
 ```
 DB_NAME = 'YOUR_DB_SCHEMA'
 DB_USER = 'YOUR_DB_USER'
 DB_PASSWORD = 'YOUR_DB_PASSWORD'
 EXTERNAL_DB = True
```
_These are the login credentials you use to connect to your local database. Also note, that you need to create the schema with the name you specified on `DB_NAME`_

Finally, run the migrations:

```python manage.py makemigrations && python  manage.py migrate ```

 And run the server
 
`python manage.py runserver`


### Populating the DB:

Initially, the database will be empty, as no shelters have been added to it. In order to read the current ones out of the json file, run the following commands :

```
python manage.py shell
from sleepez.utils import *
update_shelters()
```
## Preview 

<img src="https://user-images.githubusercontent.com/23161228/39503269-09b23238-4d93-11e8-9cd4-1d0dcf91985b.png">
