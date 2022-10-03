from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key= 'counterkey'

@app.route('/')
def count():
    return render_template("index.html")

@app.route('/press_btn')
def press_btn():

    if "visits" in session:
        session["visits"]+=1
    else:
        session["visits"]=1
    return redirect ('/display')

@app.route('/display')
def display():
    return render_template("/index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect ("/press_btn")








if __name__=="__main__":
    app.run(debug=True)