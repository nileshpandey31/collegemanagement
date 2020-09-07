from flask import Flask,render_template,request,redirect
import csv
import win32api

app = Flask(__name__)
filename = "student.csv"




@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/add',methods=['POST','GET'])
def addpage():
    entry=True
    if request.method == 'POST' :
        sid = request.form['sid']
        sname = request.form['sname']
        gender = request.form['gender']
        dob = request.form['dob']
        city = request.form['city']
        state = request.form['state']
        email = request.form['email']
        qual = request.form['qual']
        stream = request.form['stream']
        a=[[sid,sname,gender,dob,city,state,email,qual,stream]]
        with open(filename, mode='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if sid==lines[0]:
                    entry=False
                    break
                else:
                    entry=True
        if entry:
            with open(filename, 'a',newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(a)
            print(a)
        else:
            
            win32api.MessageBox(0, 'Two Student annot haveommon Id', 'ERROR')
        return redirect('/index')
    else:
        
        return render_template('add-student.html')

@app.route('/search-student',methods=['POST','GET'])
def search():
    data=[]
    if request.method=="POST":
        
        sid=request.form['sid']
        
        with open(filename, mode='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] == sid:
                    data=lines
                    #print(data)
        return  render_template('search-student.html',data=data)
    else:
        
        return render_template('search-student.html',data=data)

@app.route('/display-student')
def display():
    with open(filename, mode='r')as file:
            csvFile = csv.reader(file)
            return render_template('display-student.html',csvfile=csvFile)
    
    


    

if __name__=="__main__":
    app.run(debug=True)