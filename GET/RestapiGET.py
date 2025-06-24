from flask import Flask
from flask_restful import Resource,Api
import pymysql
app=Flask(__name__)
api=Api(app)


class CustomersInfo(Resource):
    def get(self,nm):
        dict={}
        con=pymysql.connect(host='mysql-gaurav-hirulkargaurav348-6e84.h.aivencloud.com',user='avnadmin',port=26168, password='AVNS_liKX8-67OO77oJC7wH4', database='restapi')
        curs=con.cursor()
        curs.execute(f"select * from Customer where id={nm}")
        data=curs.fetchone()
        if data:
            dict['name']=data[1]
            dict['branch']=data[4]
        else:
            dict['name']='Null'
            dict['branch']="null"
        con.close()
        return dict
api.add_resource(CustomersInfo,'/customer/info/<nm>')
app.run(debug=True)

      