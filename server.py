from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<page_name>')
def works(page_name):
    return render_template(page_name)

