from app import application
from flask_restx import Resource, Api, fields
import requests
import json


app.config.SWAGGER_UI_JSONEDITOR = True

api = Api(app, version='1.10', title='Bank IFSC API',
          description='Standalone API Wrapper for Bank IFSC Codes', contact='kumarshivam192@gmail.com', default="Main API", default_label='Namespace'
          )

ifsc = api.model("IFSC", {"IFSC": fields.String(
    "KARB0000001", description='Enter The IFSC Code', required=True)})


@api.route('/ifsc')
class HelloWorld(Resource):
    @api.expect(ifsc)
    def put(self):
        inp = api.payload["IFSC"]
        res = f"https://ifsc.razorpay.com/{inp}"
        req = requests.get(res)
        data = req.json()
        return data


if __name__ == '__main__':
    app.run(debug=True)
