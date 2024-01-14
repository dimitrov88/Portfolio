import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask.cli import load_dotenv
from flask_bootstrap import Bootstrap5
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route('/resume.html')
def resume():
    return render_template('resume.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Access form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            # Construct the email message
            subject = 'New Contact Form Submission'
            body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            sender_email = my_email
            recipients = [my_email]  # Add recipient email address

            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            connection.sendmail(sender_email, recipients, msg.as_string())

    return render_template('contact.html')


@app.route('/projects.html')
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
