import python_jsonschema_objects as pjs
import json
import sys


class Problemdetails():

    problemdetail = None
    refschema = "" 

    def __init__(self,title,status):
        self.refschema ={"title": "problem schema", "$ref" : "#/components/schemas/ProblemDetails"}
        f = open("TS29510_Nnrf_NFManagement.json","r")
        try:
            output = f.read()
            base_schema = json.loads(output)
            self.refschema.update(base_schema)
            builder = pjs.ObjectBuilder(self.refschema)
            ns = builder.build_classes()
            problemdetail_class = ns.Problemdetails
            self.invalidparam_class = ns.Invalidparam
            self.problemdetail = problemdetail_class(title=title,status=status)
        except:
            print("Exception", sys.exc_info()[0])
            return


    def set_title(self,title):
        self.problemdetail.title = title

    def set_cause(self,cause):
        self.problemdetail.cause = cause

    def set_type(self,type):
        self.problemdetail.type = type

    def set_detail(self,detail):
        self.problemdetail.detail =detail 

    def set_status(self,status):
        self.problemdetail.status = status

    def set_instance(self,instance):
        self.problemdetail.instance = instance

    def set_invalidparams(self,param,reason):
        invalidparam_instance = self.invalidparam_class(param=param,reason=reason)
        if self.problemdetail.invalidParams:
            self.problemdetail.invalidParams.append(invalidparam_instance)
        else:
            self.problemdetail.invalidParams = [invalidparam_instance]

    def set_supportedfeatures(self,feature_bitmask):
        self.problemdetail.supportedFeatures = feature_bitmask

    def jsonify(self):
        return self.problemdetail.serialize(sort_keys=True)

