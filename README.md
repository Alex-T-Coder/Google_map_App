# django-google-maps
Basic example of how to use google maps with django

![](https://raw.githubusercontent.com/LegolasVzla/django-google-maps/master/core/frontend/static/media/app_image.jpeg "App Image")

## Technologies
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

- [PostgreSQL](https://www.postgresql.org/) is the World's Most Advanced Open Source Relational Database.

- [PostGIS](http://postgis.net/) is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

## Requirements
- Ubuntu 18
- Install PostgreSQL:
```
  sudo apt-get update
  sudo apt install python3-dev postgresql postgresql-contrib python3-psycopg2 libpq-dev
```
- Install PostGIS
```
  sudo apt-get install postgis
```

## Installation

Clone this project:

	git clone https://github.com/LegolasVzla/django-google-maps.git

Create your virtualenv and install the requirements:

	virtualenv env --python=python3
	source env/bin/activate

	pip install -r requirements.txt

In "django-google-maps/core/" path, create logs folder:

	mkdir logs

Create a **settings.ini** file, with the structure as below:

	[postgresdbConf]
	DB_ENGINE=django.contrib.gis.db.backends.postgis
	DB_NAME=dbname
	DB_USER=user
	DB_PASS=password
	DB_HOST=host
	DB_PORT=port

	[googleMapsConf]
 	API_KEY=yourGoogleAPIKey
	defaultLat=<Your_default_latitude>
 	defaultLng=<Your_default_lingitude>

By default, DB_HOST and DB_PORT in PostgreSQL are localhost/5432.

Then, run the migrations:

	python manage.py makemigrations

	python manage.py migrate

And finally, run the server:

	python manage.py runserver

You could see the home page in:

	http://127.0.0.1:8000/index/

The map will be setting in the defaultLat and defaultLng position.

## Models

- Spots: table to store places of the users. This table contains a position (PostGIS geometry) column that works to store information of latitude and longitude in WGS 84 format.

## Actions

1. Add a custom place (CREATE): in "GoogleMaps" tab, you can create a new spot doing click in a position of the map and then doing click in "Add a Place" buttom, fill up the form and save your spot.

2. See spots details (READ): in "My Spot List" tab, you can see all the details of your spot list. 

3. Remove a place (DELETE): in "My Spot List" tab, you can delete an spot in the garbage icon.

4. Show nearby places: in "GoogleMaps" tab, you can display nearby places from your current position wihint 5 kilometers of distance. The map will show your nearby places with the icon below:
![](https://raw.githubusercontent.com/LegolasVzla/django-google-maps/master/core/frontend/static/media/place_icon.png "Custom Spot")

## Contributions
------------------------

I started this project from [yt-google-maps-1](https://github.com/Klerith/yt-google-maps-1) repository.

All work to improve performance is good

Enjoy it!
