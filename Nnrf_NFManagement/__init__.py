from quart import jsonify
from quart import make_response, Quart, render_template, url_for
from nf_register import nfregister
from quart import Quart,request, g
from quart_openapi import Pint, Resource
from schema import Schema
from problemdetail import Problemdetails
import json

update_patch_schemaref = '#/paths/~1nf-instances~1{nfInstanceID}/patch/requestBody/content/application~1json-patch+json/schema'
register_put_schemaref = '#/paths/~1nf-instances~1{nfInstanceID}/put/requestBody/content/application~1json/schema'

#app = Quart(__name__)
app = Pint(__name__, title='NRF Simulator')

@app.route('/')
class Root(Resource):
    async def get(self):
        response="Nnrf_NFManagement Service\n"
        return response
@app.route('/nnrf-nfm/v1/nf-instances/<instanceid>',methods=['PUT'])
class Register(Resource):
    async def put(self,instanceid):
        response="register instance "+instanceid+"\n"
        print(response)
        nfprofile = await request.get_json(force=True)
        schema = Schema(register_put_schemaref)
        result,error = schema.verify_content(nfprofile)
        if not result:
            problemdetail = Problemdetails("Bad Request",400)
            problemdetail.set_cause("INVALID_MSG_FORMAT")
            problemdetail.set_detail("Bad Request")
            problemdetail.set_type = problemdetail.set_instance = "about:blank"
            for i in range(0,len(error)):
                param = schema.prepare_param(error[i])
                reason = schema.prepare_reason(error[i])
                problemdetail.set_invalidparams(param,reason)
            response = await make_response(problemdetail.jsonify(),400,{'Content-Type': 'application/problem+json'})
            return response
        nfprofile['heartBeatTimer'] = 20
        response = await make_response(jsonify(nfprofile),200,{'Content-Type': 'application/json'})
        return response


@app.route('/nnrf-nfm/v1/nf-instances/<instanceid>',methods=['GET'])
class Get(Resource):
    async def get(self,instanceid):
        response="get instance"+" "+instanceid+"\n"
        print(response)
        getbody = open("getbody.json").read()
        getjson = json.loads(getbody)
        getjson["nfInstanceId"] = instanceid
        getjson['heartBeatTimer'] = 20
        response = await make_response(jsonify(getjson),200,{'Content-Type': 'application/json'})
        return response

@app.route('/nnrf-nfm/v1/nf-instances/<instanceid>',methods=['PATCH'])
class Update(Resource):
    async def patch(self,instanceid):
        response="update instance"+" "+instanceid+"\n"
        print(response)
        patchbody = await request.get_json(force=True)
        schema = Schema(update_patch_schemaref)
        result,error = schema.verify_content(patchbody)
        if not result:
            problemdetail = Problemdetails("Bad Request",400)
            problemdetail.set_cause("INVALID_MSG_FORMAT")
            problemdetail.set_detail("Bad Request")
            problemdetail.set_type = problemdetail.set_instance = "about:blank"
            for i in range(0,len(error)):
                param = schema.prepare_param(error[i])
                reason = schema.prepare_reason(error[i])
                problemdetail.set_invalidparams(param,reason)
            response = await make_response(problemdetail.jsonify(),400,{'Content-Type': 'application/problem+json'})
            return response
        response = await make_response('',204)
        return response
@app.route('/nnrf-nfm/v1/nf-instances/<instanceid>',methods=['DELETE'])
class Delete(Resource):
    async def delete(self,instanceid):
        statement="deregister instance"+" "+instanceid+"\n"
        print(statement)
        response = await make_response('',204)
        return response


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8443,
        certfile='apache-selfsigned.pem',
        keyfile='apache-selfsigned.key',
    )
