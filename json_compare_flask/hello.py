"""
NAME: hello.py
DESCRIPTION: This module executes a web application using flask that 
compares 2 JSON data inputs.
Version  Date             Developer        Comments                         
1.0      12/08/2017       sjimenez         - Initial release 
"""
from flask import Flask, render_template, request, url_for
from wtforms import Form, StringField
import json
import json_compare #Required to execute the comparison logic 

app = Flask(__name__)

#Welcome page
#Welcomes the user and gives information about the application.
#Contains the button/link to the comparison page
#Go to /templates/welcome.html for more information
@app.route('/')
def welcome():
    return render_template('welcome.html')

#Input page
#Contains the input boxes to enter data and the compare button. This 
#  executes logic under "action" function. 
#Go to /templates/form_submit.html for more information
@app.route('/endpoint1', methods=['POST','GET'])
def form():
    return render_template('form_submit.html')

#Results page
#This shows the results based on json_compare imported module logic.
#Includes a Back button for new comparisons.
@app.route('/action', methods=['POST','GET'])
def action():
    """
    DESCRIPTION: Executes 2 JSONS data comparisons:equal, different size
                 and differences.
    ARGUMENTS: - json1, json2 (str) Encoded jsons data string from 
                                    form_action.html
    RETURNS:  - result (str)    Comparison results in json format or
                                errors of the execution due to 
                                incorrect data format
    """                         
    json1=request.form['json1']
    json2=request.form['json2']
    if json1 == '' or json2 == '':
        result = 'There is an empty input field!'
        return render_template('form_action.html', result=result)  
    try:
        jc = json_compare.JsonCompare(json1,json2)
        if jc.equal()[0]:   #Check if both jsons are equal
            print(jc.equal()[1])
            result = jc.equal()[1]
        
        elif jc.same_size()[0]: #If different, check for size.
            print(jc.diff())
            result = jc.diff()
        
        else: #If same size but different, check for differences.
            print(jc.same_size()[1])
            result = jc.same_size()[1]
        return render_template('form_action.html', result=result)                
    
    except json.decoder.JSONDecodeError as inst: #Catch data format errors 
        result= ('There is an error with the JSON data, probably not' +
                ' in the correct format. Here is the error: ' + 
                str(inst))
        return render_template('form_action.html', result=result)
    except Exception as inst: #Catch unhandled exceptions
        result = ('An unhandled error occurred. Here is the ERROR: ' + 
                  str(inst))
        return render_template('form_action.html', result=result)

#Defining function for future release.
# @app.route('/create_json/', methods=['POST'])
# def create_json():
#     pass

if __name__== '__main__':
    app.run(debug=True)
