"""
NAME: json_compare.py
DESCRIPTION: This module contains functions for json data comparison
Version  Date             Developer        Comments                         
1.0      12/08/2017       sjimenez         - Initial release 
"""
import json

class JsonCompare:
    """ 
    DESCRIPTION: Contains the functions for jsons comparison
    ARGUMENTS: json1, json2 (json) JSON encoded data 
    """
    def __init__(self, json1, json2):         
        self.djson1 = json.loads(json1) #Converts json to python dict
        self.djson2 = json.loads(json2)

    def equal(self):
        """ 
        DESCRIPTION: Check if 2 jsons are equal
        RETURNS: [BOOL, json] 
                 BOOL: TRUE if both jsons are equal, FALSE if not
                 json: json with result
        """
        if self.djson1 == self.djson2:
            result = True
        else:
            result = False
        message = {'Equal?': result}
        #Convert message to json format
        jmessage = json.dumps(message, indent=6, sort_keys=True)
        return result, jmessage
    
    def same_size(self):
        """ 
        DESCRIPTION: Check if 2 jsons are of same size
        RETURNS: [BOOL, json] 
                 BOOL: TRUE if both jsons are same size, FALSE if not
                 json: json with result
        """
        if len(self.djson1) == len(self.djson2):
            result = True
        else:
            result = False
        message = {'Same size?': result}
        #Convert message to json format
        jmessage = json.dumps(message, indent=6, sort_keys=True)
        return result, jmessage

    def diff(self):
        """ 
        DESCRIPTION: Check where differences are in 2 jsons
        RETURNS: json - 
                 {'Same keys': keys that contain same data
                  'Missing keys in json1': Keys that are in json2 that 
                                           are not in json1
                  'Missing keys in json1': Keys that are in json1 that
                                           are not in json2
                  'Same keys with differences': Keys that contains 
                                                different data
                 }
        """        
        djson1_keys = set(self.djson1.keys()) #Obtain keys of dict
        djson2_keys = set(self.djson2.keys())
        #Find same keys in both dict
        same_keys   = djson1_keys.intersection(djson2_keys)
        #Sort result to have the same output everytime 
        lsame_keys =sorted(list(same_keys))
        #Missing keys in both jsons (sort them)
        json1_missing_keys  = sorted(list(djson2_keys - same_keys)) 
        json2_missing_keys  = sorted(list(djson1_keys - same_keys))
        #Keys with differences
        diff_keys = [] #Create empty list
        for k in same_keys:
            if self.djson1[k] != self.djson2[k]:
                diff_keys.append(k)
        #Build results dict
        results = {'Same keys' : lsame_keys,
                   'Missing keys in json1' : json1_missing_keys,
                   'Missing keys in json2' : json2_missing_keys, 
                   'Same keys with differences': sorted(diff_keys)}
        message = {'Compare results': results}
        #Convert message to json format
        jmessage = json.dumps(message, indent=6, sort_keys=True)
        return jmessage

#CODE FOR TESTING PURPOSES
# if __name__ == '__main__':
#  
#     json_1= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": 2,"aboolean": true, "boolean": true,"object": {"foo": "bar","object1": {"new prop1": "new prop value"},"object2": {"new prop1": "new prop value"},"object3": {"new prop1": "new prop value"},"object4": {"new prop1": "new prop value"}}},"Amy Ryan": {"one": "In Treatment","two": "The Wire"},"Annie Fitzgerald": ["Big Love","True Blood"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsgard": ["Generation Kill","True Blood"], "Clarke Peters": null}' 
#     json_2= '{"Aidan Gillen": {"array": ["Game of Thrones","The Wire"],"string": "some string","int": "2","otherint": 4, "aboolean": "true", "boolean": false,"object": {"foo": "bar"}},"Amy Ryan": ["In Treatment","The Wire"],"Annie Fitzgerald": ["True Blood","Big Love","The Sopranos","Oz"],"Anwan Glover": ["Treme","The Wire"],"Alexander Skarsg?rd": ["Generation Kill","True Blood"],"Alice Farmer": ["The Corner","Oz","The Wire"]}' 
#     jc = JsonCompare(json_1,json_2)
#     if jc.equal()[0]:
#         print(jc.equal()[1])
#     elif jc.same_size()[0]:
#         print(jc.diff())
#     else:
#         print(jc.same_size()[1])
         
        
    