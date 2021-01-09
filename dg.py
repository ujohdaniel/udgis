# Importing the modules
from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

# Creating the app
app= Flask(__name__)

sentry_sdk.init(
    dsn="https://c67ee328a7434792be2f90183f83d7ed@o502257.ingest.sentry.io/5584444",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

# Home page
@app.route('/')
def homepage():
    return render_template('home.html')

# Events page
@app.route('/events')
def events():
    return render_template('events.html')

# Gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# About us page
@app.route('/aboutus')
def about():
    return render_template('about.html')

# Contact us page
@app.route('/admissions')
def contact():
    return render_template('admissions.html')

# Services page
@app.route('/services')
def services():
    return render_template('services.html')

# On debug mode
if __name__ == '__main__':
    app.run(debug=True)
