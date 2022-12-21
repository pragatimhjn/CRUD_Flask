'''
#env\Scripts\activate--> activate virtual env before running this file on cmd
'''
from flask import Flask,render_template,request,redirect
import pymysql as p                                        

app=Flask('__name__')                                        #creating intance of Flask Class,this instance will be our app


""" ******************************* index/homepage *************************************************************************   """

@app.route('/')
def home():
    try:
     db=p.connect(host="localhost",user="root",password="",database="healthcare")
     c=db.cursor()
     q="select * from patients"                         #selecting all records for display
     c.execute(q)
     data=c.fetchall()
     return render_template('index.html',d=data)
    
    except Exception as e:
      print("Error:",e)

@app.route('/create')
def create():

    return render_template('create_record.html')         #html structure for create task interface






"""********************************* store/save *******************************************   """ 

@app.route('/store',methods=['POST'])                   #get--> reveals user data in url,post-->no user data in url
def store():

    #return "Inside store record section "              #-> initial checking
    name=request.form['name']
    date=request.form['date']
    bg=request.form['bg']
    gender=request.form['gender']
    sym=request.form.getlist('symptoms')
    symptom=','.join(sym)    
    
    try:
         db=p.connect(host="localhost",user="root",password="",database="healthcare")
         c=db.cursor()
         q="insert into patients(name,birthdate,bloodgroup,gender,symptoms)values('{}','{}','{}','{}','{}')".format(name,date,bg,gender,symptom)
         c.execute(q)
         db.commit()
         #return "Record inserted successfully"
         return redirect('/')
    except Exception as e:
         print("Error:",e)

""" ************************************* edit_record_interface **************************************** """     
@app.route('/edit/<rid>')             
def edit(rid):
    
    #return "Id to be edited:"+rid                  #-> initial checking
    try:
     db=p.connect(host="localhost",user="root",password="",database="healthcare")
     c=db.cursor()
     q="select * from patients where id='{}'".format(rid)      #selecting record to be edited
     c.execute(q)
     data=c.fetchone()
     return render_template('edit_record.html',d=data)
    except Exception as e:
      print("Error:",e)

""" *********************************************** edit_operation *************************** """

@app.route('/update/<rid>',methods=['Post'])             #for every patial part of url *html page
def update(rid):
    #return "Id to be updated:"+rid
  try:
    db=p.connect(host="localhost",user="root",password="",database="healthcare")
    c=db.cursor()
    name=request.form['name']
    date=request.form['date']
    bg=request.form['bg']
    gender=request.form['gender']
    sym=request.form.getlist('symptoms')
    symptom=','.join(sym)    
    q="update patients SET name='{}',birthdate='{}',bloodgroup='{}',gender='{}',symptoms='{}' where id='{}'".format(name,date,bg,gender,symptom,rid)
    c.execute(q)
    db.commit()
    return redirect('/')
  except Exception as e:   
    print("Error:",e)

"""   ************************************************* delete ****************************** """

@app.route('/delete/<rid>')             #for every patial part of url *html page
def delete(rid):
    
    #return "Id to be deleted:"+rid
  try:
     db=p.connect(host="localhost",user="root",password="",database="healthcare")
     c=db.cursor()
     q="delete from patients where id='{}'".format(rid)
     c.execute(q)
     db.commit()
     return redirect('/')
  except Exception as e:
      print("Error:",e)

       
app.run(debug=True)







