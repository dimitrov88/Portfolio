from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route('/resume.html')
def resume():
    return render_template('resume.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/projects.html')
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
