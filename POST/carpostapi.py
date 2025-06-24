from flask import Flask,request
import pymysql

app=Flask(__name__)


@app.route('/owner/add',methods=['POST'])
def caradd():
    id=int(request.form.get("ownerid",0))
    nm=request.form.get("name")
    crnm=request.form.get("carname")
    crid=request.form.get("carid")
    pr = float(request.form.get("price") or 0.0)

    dict={}
    try:
        id = int(id)
        pr = float(pr)
        con=pymysql.connect(host='mysql-gaurav-hirulkargaurav348-6e84.h.aivencloud.com',user='avnadmin',port=26168, password='AVNS_liKX8-67OO77oJC7wH4', database='restapi')
        curs=con.cursor()
        curs.execute(f"Insert into owner(ownerid,name,carname,carid,price) values({id},'{nm}','{crnm}','{crid}',{pr})")
        con.commit()
        con.close()
        dict['message']="Inserted Successfully"

    except Exception as e:
        dict['message'] = "Not Inserted"
        dict['error'] = str(e)
    return dict
app.run(debug=True)    