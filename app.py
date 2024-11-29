from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

app.run(debug=True, port=4000)