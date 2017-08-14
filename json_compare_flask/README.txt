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
	- wtforms -> From cmd line type: -> pip install wtforms

Instructions:
	From cmd:
	1.- Go to the project folder(previously downloaded):
		Windows/Linux: 
			$ cd C:\<project>\<folder>\<path>\json_compare_flask
	2.- Activate venv:
		Windows:
			$ venv\Scripts\activate
		Linux:
			$ chmod +x venv\Scripts\activate
	3.- Export FLASK_APP environment variable:
		Windows:
			$ set FLASK_APP=hello.py
		Linux:
			$ export FLASK_APP=hello.py
	4.- Run the application
		Windows/Linux: 
			$ flask run
	5.- Go to http://127.0.0.1:5000/ from a browser 
	6.- All set, you can now compare json data!

Future releases features:
1.1   - Add a json data generator from a url or a file. Data can be use
        to test the application.
1.2   - Provide more insight into the differences.
	  - Provide more insight into the format of an incorrect json data input   

Author
	Salvador Jiménez Noriega - nojiso@gmail.com

