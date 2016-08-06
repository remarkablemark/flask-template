#!/usr/bin/env python

from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    context = { 'name': 'Flask' };
    return render_template('index.html', **context)

app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
