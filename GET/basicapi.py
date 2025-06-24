from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class BasicApi(Resource):
    def get(self):
        information={
            "name":"Gaurav hirulkar",
            "age":20,
            "college":"Sipna Coet",
            "branch":"CSE",
            "skill":"python Developer",
            "mobileno":9322482903,
            "CGPA":9.60,
            "city":"Amravati",
            "subject":"Python"
        }
        return information
api.add_resource(BasicApi,'/profile')
app.run(debug=True)