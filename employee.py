from flask import Flask, render_template,request,redirect,url_for
from datetime import datetime
#import pandas as pd
#import numpy as np



import sqlite3
app=Flask(__name__)
# conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
conn=sqlite3.connect('/Users/mohammadshaik/Desktop/Mohammad/Python Projects/Attendance/employee.db')
conn.close()
@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/newemployee')
def newemployee():
    return render_template('employee.html')


@app.route('/addemployee', methods=['POST'])
def addemployee():
        #try:
        conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
        cur=conn.cursor()
        ID=request.form['EMP_ID']
        DESIGNATION_ID=request.form['EMP_DESIGNATION_ID']
        FIRST_NAME=request.form['EMP_FIRST_NAME']
        MIDDLE_NAME=request.form['EMP_MIDDLE_NAME']
        LAST_NAME=request.form['EMP_LAST_NAME']
        MANAGER_ID=request.form['EMP_MANAGER_ID']
        HIRE_DATE=request.form['EMP_HIRE_DATE']
        RESIGNED_DATE=request.form['EMP_RESIGNED_DATE']
        D_O_B=request.form['EMP_D_O_B']
        SALARY_INR=request.form['EMP_SALARY_INR']
        BANK_ACT_NO=request.form['EMP_BANK_ACT_NO']
        BANK_NAME=request.form['EMP_BANK_NAME']
        BANK_BRANCH=request.form['EMP_BANK_BRANCH']
        BANK_IFSC_CODE=request.form['EMP_BANK_IFSC_CODE']
        ACTIVE_ASSIGNMENT=request.form['EMP_ACTIVE_ASSIGNMENT']
        GENDER=request.form['EMP_GENDER']
        ADDRESS=request.form['EMP_ADDRESS']
        PHONE_NO=request.form['EMP_PHONE_NO']
        EMAIL=request.form['EMP_EMAIL'] 
        LAST_UPDATED_TIME=datetime.now()
        LAST_UPDATED_BY=request.form['EMP_FIRST_NAME']
                
        val=(ID,DESIGNATION_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,MANAGER_ID,HIRE_DATE,RESIGNED_DATE,D_O_B,SALARY_INR,BANK_ACT_NO,BANK_NAME,BANK_BRANCH,BANK_IFSC_CODE,ACTIVE_ASSIGNMENT,GENDER,ADDRESS,PHONE_NO,EMAIL,LAST_UPDATED_TIME,LAST_UPDATED_BY)
        #cur.execute("INSERT INTO admin (ad_name,ad_email,ad_pswd,ad_ph_no,ad_street,ad_city,ad_state,ad_pin) VALUES (?,?,?,?,?,?,?,?)" ,(m,n,o,p,q,r,s,t))
        cur.execute("insert into EMPLOYEE(EMP_ID,EMP_DESIGNATION_ID,EMP_FIRST_NAME,EMP_MIDDLE_NAME,EMP_LAST_NAME,EMP_MANAGER_ID,EMP_HIRE_DATE,EMP_RESIGNED_DATE,EMP_D_O_B,EMP_SALARY_INR,EMP_BANK_ACT_NO,EMP_BANK_NAME,EMP_BANK_BRANCH,EMP_BANK_IFSC_CODE,EMP_ACTIVE_ASSIGNMENT,EMP_GENDER,EMP_ADDRESS,EMP_PHONE_NO,EMP_EMAIL,EMP_LAST_UPDATED_TIME,EMP_LAST_UPDATED_BY) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",val)
                
        conn.commit()
        return "Added Employee Details Sucessfull"       
            #msg = "Record successfully added"
        '''except:
            conn.rollback()
            return "error in insert operation"
            #msg = "error in insert operation"

        finally:
            return render_template("attendance.html")
            conn.close()'''
        conn.close()


@app.route('/fetchempid')
def fetchempid():
    conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
    cur=conn.cursor()
    
    cur.execute("select EMP_ID from EMPLOYEE")
    row=cur.fetchall()
    return render_template('fetchempid.html',row=row)
    conn.close()

@app.route('/editemployee',methods=['POST'])
def editemployee():
    conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
    cur=conn.cursor()
    ID=request.form['EMP_ID']
    cur.execute("select EMP_ID,EMP_DESIGNATION_ID,EMP_FIRST_NAME,EMP_MIDDLE_NAME,EMP_LAST_NAME,EMP_MANAGER_ID,EMP_HIRE_DATE,EMP_RESIGNED_DATE,EMP_D_O_B,EMP_SALARY_INR,EMP_BANK_ACT_NO,EMP_BANK_NAME,EMP_BANK_BRANCH,EMP_BANK_IFSC_CODE,EMP_ACTIVE_ASSIGNMENT,EMP_GENDER,EMP_ADDRESS,EMP_PHONE_NO,EMP_EMAIL from EMPLOYEE where EMP_ID=='"+ID+"' ")
    rows=cur.fetchone()
    print(rows)
    return render_template('employee_update.html',rows=rows)

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        #try:
        conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
        cur=conn.cursor()
        ID=request.form['EMP_ID']
        DESIGNATION_ID=request.form['EMP_DESIGNATION_ID']
        FIRST_NAME=request.form['EMP_FIRST_NAME']
        MIDDLE_NAME=request.form['EMP_MIDDLE_NAME']
        LAST_NAME=request.form['EMP_LAST_NAME']
        MANAGER_ID=request.form['EMP_MANAGER_ID']
        HIRE_DATE=request.form['EMP_HIRE_DATE']
        RESIGNED_DATE=request.form['EMP_RESIGNED_DATE']
        D_O_B=request.form['EMP_D_O_B']
        SALARY_INR=request.form['EMP_SALARY_INR']
        BANK_ACT_NO=request.form['EMP_BANK_ACT_NO']
        BANK_NAME=request.form['EMP_BANK_NAME']
        BANK_BRANCH=request.form['EMP_BANK_BRANCH']
        BANK_IFSC_CODE=request.form['EMP_BANK_IFSC_CODE']
        ACTIVE_ASSIGNMENT=request.form['EMP_ACTIVE_ASSIGNMENT']
        GENDER=request.form['EMP_GENDER']
        ADDRESS=request.form['EMP_ADDRESS']
        PHONE_NO=request.form['EMP_PHONE_NO']
        EMAIL=request.form['EMP_EMAIL'] 
        '''s=datetime.now()
        LAST_UPDATED_TIME = s.datetime.now()'''
        '''departure_time = flights_drop_null['EMP_LAST_UPDATED_TIME']
        DST = departure_time.now()
        LAST_UPDATED_TIME = datetime.datetime.now(DST) '''   
        LAST_UPDATED_BY=request.form['EMP_FIRST_NAME']
        #print(GENDER,ADDRESS)      
        #print(datetime.now(),LAST_UPDATED_TIME)
       
        cur.execute("update EMPLOYEE SET EMP_ID= '"+ID+"',EMP_DESIGNATION_ID='"+DESIGNATION_ID+"',EMP_FIRST_NAME= '"+FIRST_NAME+"',EMP_MIDDLE_NAME= '"+MIDDLE_NAME+"',EMP_LAST_NAME= '"+LAST_NAME+"',EMP_MANAGER_ID= '"+MANAGER_ID+"',EMP_HIRE_DATE= '"+HIRE_DATE+"',EMP_RESIGNED_DATE= '"+RESIGNED_DATE+"',EMP_D_O_B= '"+D_O_B+"',EMP_SALARY_INR= '"+SALARY_INR+"',EMP_BANK_ACT_NO= '"+BANK_ACT_NO+"',EMP_BANK_NAME= '"+BANK_NAME+"',EMP_BANK_BRANCH= '"+BANK_BRANCH+"',EMP_BANK_IFSC_CODE= '"+BANK_IFSC_CODE+"',EMP_ACTIVE_ASSIGNMENT= '"+ACTIVE_ASSIGNMENT+"',EMP_GENDER= '"+GENDER+"',EMP_ADDRESS= '"+ADDRESS+"',EMP_PHONE_NO= '"+PHONE_NO+"',EMP_EMAIL= '"+EMAIL+"',EMP_LAST_UPDATED_TIME= datetime('now'),EMP_LAST_UPDATED_BY='"+LAST_UPDATED_BY+"' where EMP_ID=='"+ID+"' ")
       
        conn.commit()
        return "Updated Employee Details Sucessfull"

@app.route('/addattendance')
def addattendance():
    conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
    cur=conn.cursor()
    #cur.execute("select EMP_ID,EMP_FIRST_NAME,EMP_DESIGNATION_ID,EMP_PHONE_NO from EMPLOYEE where EMP_ID = 1")
    cur.execute("select EMP_ID,EMP_FIRST_NAME,EMP_DESIGNATION_ID,EMP_PHONE_NO from EMPLOYEE")
    rows=cur.fetchall()
    #print(rows)
    return render_template('attendance.html',rows=rows)
    conn.close()



@app.route('/saveattendance', methods=['POST'])
def saveattendance():
    conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
    cur = conn.cursor()



    CALENDAR_DATE=request.form['ATT_CALENDAR_DATE']
    

    ID=request.form['EMP_ID']
    
    PRESENT_FLAG=request.form['ATT_PRESENT_FLAG']
    SALARY_ADVANCE=request.form['ATT_SALARY_ADVANCE']

    LAST_UPDATED_TIME=datetime.now()
    LAST_UPDATED_BY=request.form['EMP_ID']

    list_attendance = []
    d = {'keys': [],'val': [],'values': []}
    f = request.form
    for key in f.keys():
        for value in f.getlist(key):
            print(key,":",value)
            d['values'].append(value)
        d['val'].append(d['values'])
        d['keys'].append(key)
            
    print(d['keys'])
    print(d['values'])
   
    #for val in rows:
    val = (ID,CALENDAR_DATE,PRESENT_FLAG,SALARY_ADVANCE,LAST_UPDATED_TIME,LAST_UPDATED_BY)
    #print(rows)
    #print(val)
    cur.executemany("insert into ATTENDANCE(EMP_ID,ATT_CALENDAR_DATE,ATT_PRESENT_FLAG,ATT_SALARY_ADVANCE,ATT_LAST_UPDATED_TIME,ATT_LAST_UPDATED_BY) values(?,?,?,?,?,?)",val)
    conn.commit()
    return "Added Attendance Details Sucessfully"

    conn.close()




'''@app.route('/saveattendance', methods=['POST'])
def saveattendance():
    conn=sqlite3.connect('C:/Users/hhh/Desktop/Python Projects/Attendance/employee.db')
    cur = conn.cursor()

    CALENDAR_DATE=request.form['ATT_CALENDAR_DATE']
    

    ID=request.form['EMP_ID']
    
    for entry in range(rows):
        entry[0] = request.form['EMP_ID']
        entry[1] = request.form['ATT_CALENDAR_DATE']
        entry[2] = request.form['ATT_PRESENT_FLAG']
        entry[3] = request.form['ATT_SALARY_ADVANCE']
        entry[4] = datetime.now()
        entry[5] = request.form['EMP_ID']
    

    

    list_attendance = []

    val = (ID,CALENDAR_DATE,PRESENT_FLAG,SALARY_ADVANCE,LAST_UPDATED_TIME,LAST_UPDATED_BY)
    cur.execute("insert into ATTENDANCE(EMP_ID,ATT_CALENDAR_DATE,ATT_PRESENT_FLAG,ATT_SALARY_ADVANCE,ATT_LAST_UPDATED_TIME,ATT_LAST_UPDATED_BY) values(?,?,?,?,?,?)",val)
    conn.commit()
    return "Added Attendance Details Sucessfully"

    conn.close()'''

if __name__ == '__main__':
   app.run(debug = True)
