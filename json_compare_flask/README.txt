JSON COMPARE TOOL
  This application uses flask to run a web interface that compares 2 json data.

Version:
1.0 - 12/08/2017

What is included in the project?
	- hello.py: Integrates the json_compare functionality into a web interface. Runs the web service.
	- json_compare.py: Module containing the application logic.
	- unit_test:   Runs the unittest of json_compare.py module.
	- Sample data: Some data to be used to try the application.
	- templates(folder):  Contains the html templates required for the interface.
	- static(folder):  Contains the .css file with the style(appearance) of html instances.
	- venv: Contains the virtual environment files(environment created on Windows 8.1)

Prerequisites
	Before running the application make sure you have previously installed:
	- python (3.5 preferred) -> Go to https://www.python.org/downloads/
	- virtualenv -> From cmd line type: pip install virtualenv
	- flask  (0.12.2 preferred) -> From cmd line type: pip install Flask 
                              (or go to http://flask.pocoo.org/docs/0.12/installation/#installation)

Instructions(for Windows):
	From cmd:
	1.- Go to the project folder(previously downloaded): 
		$ cd C:\Documents\json_compare_flask
	2.- Activate venv:
		$ venv\Scripts\activate
	3.- Export FLASK_APP environment variable:
		$ set FLASK_APP=hello.py
	4.- Run the application
		$ flask run
	5.- Go to http://127.0.0.1:5000/ in a browser 
	6.- All set, you can no compare json data!

Author
	Salvador Jiménez Noreiga - nojiso@gmail.com

