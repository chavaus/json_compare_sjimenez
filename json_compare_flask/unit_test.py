"""
NAME: unit_test.py
DESCRIPTION: This module executes unit testing to each of
             json_compare functions 
Version  Date             Developer        Comments                         
1.0      12/08/2017       sjimenez         - Initial release 
"""
import unittest
from json_compare import JsonCompare
import json

class TestJsonCompare(unittest.TestCase): #Inherit unnittest attributes
        
    def test_equal(self):
        """
        TO TEST: json_compare.JsonCompare.equal
        PASS TEST CRITERIA: 
            1.- equal(json1_test,json1_test)[0] returns TRUE
            2.- equal(json1_test,json2_test)[0] returns FALSE
            3.- equal(json1_test,json1_test)[1] returns 
                                                json_result_equal
            4.- equal(json1_test,json2_test)[1] returns 
                                                json_result_different
        """ 
        #Test arguments
        json1_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": 2,"aboolean": true, "boolean": true,"object": {"foo": "bar","object1": {"new prop1": "new prop value"},"object2": {"new prop1": "new prop value"},"object3": {"new prop1": "new prop value"},"object4": {"new prop1": "new prop value"}}},"Amy Ryan": {"one": "In Treatment","two": "The Wire"},"Annie Fitzgerald": ["Big Love","True Blood"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsgard": ["Generation Kill","True Blood"], "Clarke Peters": null}'  
        json2_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": "2","otherint": 4, "aboolean": "true", "boolean": false,"object": {"foo": "bar"}},"Amy Ryan": ["In Treatment","The Wire"],"Annie Fitzgerald": ["True Blood","Big Love","The Sopranos","Oz"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsg?rd": ["Generation Kill","True Blood"],"Alice Farmer": ["The Corner","Oz","The Wire"]}'
        equal = [json1_test,json1_test]  #Equal data set
        different = [json1_test,json2_test] #Different data set
        #Return[1] from equal data set eval
        json_result_equal = '{\n      "Equal?": true\n}'
        #Return[1] from different data set eval 
        json_result_different = '{\n      "Equal?": false\n}'
        
        #Tests
        self.assertTrue(JsonCompare(*equal).equal()[0])
        self.assertFalse(JsonCompare(*different).equal()[0])             
        self.assertEqual(JsonCompare(*equal).equal()[1],
                         json_result_equal)
        self.assertEqual(JsonCompare(*different).equal()[1],
                         json_result_different)  
    
    def test_samesize(self):
        """
        TO TEST: json_compare.JsonCompare.samesize
        PASS TEST CRITERIA: 
            1.- samesize(json1_test,json1_test)[0] returns TRUE
            2.- samesize(json1_test,json2_test)[0] returns FALSE
            3.- samesize(json1_test,json1_test)[1] returns 
                                                    json_result_equal
            4.- samesize(json1_test,json2_test)[1] returns 
                                                 json_result_different
        """ 
        #Test arguments
        json1_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": 2,"aboolean": true, "boolean": true,"object": {"foo": "bar","object1": {"new prop1": "new prop value"},"object2": {"new prop1": "new prop value"},"object3": {"new prop1": "new prop value"},"object4": {"new prop1": "new prop value"}}},"Amy Ryan": {"one": "In Treatment","two": "The Wire"},"Annie Fitzgerald": ["Big Love","True Blood"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsgard": ["Generation Kill","True Blood"], "Clarke Peters": null}'  
        json2_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": "2","otherint": 4, "aboolean": "true", "boolean": false,"object": {"foo": "bar"}},"Amy Ryan": ["In Treatment","The Wire"],"Annie Fitzgerald": ["True Blood","Big Love","The Sopranos","Oz"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsg?rd": ["Generation Kill","True Blood"]}'
        equal = [json1_test,json1_test] #Equal data set
        different = [json1_test,json2_test] #Different data set
        #Return[1] from equal data set eval
        json_result_equal = '{\n      "Same size?": true\n}'
        #Return[1] from equal data set eval
        json_result_different = '{\n      "Same size?": false\n}'
        
        #Test        
        self.assertTrue(JsonCompare(*equal).same_size()[0])
        self.assertFalse(JsonCompare(*different).same_size()[0])
        self.assertEqual(JsonCompare(*equal).same_size()[1],
                         json_result_equal)
        self.assertEqual(JsonCompare(*different).same_size()[1],
                         json_result_different)  
 
    def test_diff(self):
        """
        TO TEST: json_compare.JsonCompare.diff
        PASS TEST CRITERIA: 
            ** Convert .diff results to dict for correct .assertEqual
               functionality
            1.- dictionary of diff(json1_test,json2_test) == 
                                                     json_expected_dict  
        """ 
        #Test arguments
        json1_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": 2,"aboolean": true, "boolean": true,"object": {"foo": "bar","object1": {"new prop1": "new prop value"},"object2": {"new prop1": "new prop value"},"object3": {"new prop1": "new prop value"},"object4": {"new prop1": "new prop value"}}},"Amy Ryan": {"one": "In Treatment","two": "The Wire"},"Annie Fitzgerald": ["Big Love","True Blood"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsgard": ["Generation Kill","True Blood"], "Clarke Peters": null}' 
        json2_test= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": "2","otherint": 4, "aboolean": "true", "boolean": false,"object": {"foo": "bar"}},"Amy Ryan": ["In Treatment","The Wire"],"Annie Fitzgerald": ["True Blood","Big Love","The Sopranos","Oz"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsg?rd": ["Generation Kill","True Blood"],"Alice Farmer": ["The Corner","Oz","The Wire"]}'
        json_expected_dict = {'Compare results': {'Missing keys in json2': ['Alexander Skarsgard', 'Clarke Peters'], 'Same keys': ['Aidan Gillen', 'Amy Ryan', 'Annie Fitzgerald', 'Anwan Glover'], 'Missing keys in json1': ['Alexander Skarsg?rd', 'Alice Farmer'], 'Same keys with differences': ['Aidan Gillen', 'Amy Ryan', 'Annie Fitzgerald']}}
        json_dict= json.loads(JsonCompare(json1_test,json2_test).diff())
        #Test
        self.assertEqual(json_dict, json_expected_dict)
       
if __name__=='__main__':        
    unittest.main()
    

    
    
    