from flask import Flask, redirect, url_for, render_template
# to run, run in command prompt the copy link in cmd or go to http://127.0.0.1:5000/
#HTML Template is in Templates folder, must be called Templates
#content= value passed into return arg, changes content value in html file


app = Flask(__name__)


@app.route("/<name>")
def name(name):
    return render_template('index2.html')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
    
    