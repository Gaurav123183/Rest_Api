from flask import Flask,request
import pymysql
app=Flask(__name__)
@app.route("/delete/profile", methods=["DELETE"])
def deleteProfile():
   acc=int(request.form.get("accno"))
   dict={}

   try:
       con=pymysql.connect(host='mysql-gaurav-hirulkargaurav348-6e84.h.aivencloud.com',user='avnadmin',port=26168, password='AVNS_liKX8-67OO77oJC7wH4', database='restapi')
       curs=con.cursor()
       curs.execute(f"delete from accounts where accno={acc}") 
       con.commit()
       curs.close()
       dict['message']="Account is deleted successfully"
   except:
       dict['message']="Account is not deleted"
   return dict
app.run(debug=True)
       
     
      
