from flask import Flask,request
import pymysql


app=Flask(__name__)
@app.route('/money/transfer',methods=['PUT'])


def moneyTransfer():
    fraccno=int(request.form.get("fromacc"))
    # toaccno=int(request.form.get("toacc"))
    amt=float(request.form.get("amount"))
    # bal=float(request.form.get("balance"))
    dict={}


    try:
        con=pymysql.connect(host='mysql-gaurav-hirulkargaurav348-6e84.h.aivencloud.com',user='avnadmin',port=26168, password='AVNS_liKX8-67OO77oJC7wH4', database='restapi')
        curs=con.cursor()
        curs.execute(f"update transfer set balance=balance-{amt} where fromacc={fraccno}")
        curs.execute(f"update transfer set balance=balance+{amt} where toacc={fraccno}")
        con.commit()
        con.close()
        dict['message']='updated'
    except:
        dict['message']='not updated'
    return dict
app.run(debug=True)
 