# pip install flask module
# run "$env:FLASK_APP = "main.py" in terminal (specific for powershell in PYCharm)
# run "$env:FLASK_DEBUG = "1" in terminal to enable debug mode(active server that changes upon refresh)
# html file should be in a "templates" folder
# css & js files save under the static folder
# run "flask run" in terminal
# 127.0.0.1:5000

from flask import Flask, render_template, url_for , request, redirect # imports the flask library
import csv

app = Flask(__name__)  # created a object of server type

@app.route('/')  # accesses the main route on the site (127.0.0.1:5000)
def myhome():
    return render_template('index.html')  # runs the html file in the template folder

@app.route('/<string:pagename>')  # accesses the pages dynamically (not needed to make a route for every page
def htmlpage(pagename):
    return render_template(pagename)

def writetofile(data):
    with open('database.txt', mode='a')as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{email},{subject},{message}')

def writetocsv(data):
    with open('database.csv', mode='a',newline='')as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submitform', methods=['POST','GET'])
def submitform():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            writetofile(data)
            writetocsv(data)
            return redirect('thankyou.html')
        except:
            return'did not save to database'
    else:
        return 'something went wrong.'