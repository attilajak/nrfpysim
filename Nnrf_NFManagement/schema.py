from jsonschema import validate
import jsonschema
import json
import sys
from collections import deque

class Schema():

    def __init__(self,schemaref):

        self.refschema={"$ref": schemaref}

        f = open("TS29510_Nnrf_NFManagement.json","r")

        try:
            output = f.read()
            stdschema = json.loads(output)
        except:
            return None,sys.exc_info()[0]
        else:
            self.refschema.update(stdschema)

        finally:
            f.close()


    def prepare_param(self,error):
        absolute_path = error.absolute_path
        param = "["
        for i in range (0,len(absolute_path)):
            param += str(absolute_path[i])+"]["
        print(error.instance)
        param += json.dumps(error.instance)+"]"
        return param

    def prepare_reason(self,error):
        reason = error.message
        return reason

    def verify_content(self,content):
        try:
            instance = content 
            v = jsonschema.Draft7Validator(self.refschema)
            errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
        except jsonschema.exceptions.ValidationError as e:
            return False,[e]
        else:
            if not errors:
                return True,[]
            else:
                print(errors)
                return False,errors
