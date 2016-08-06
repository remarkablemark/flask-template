#!/usr/bin/env python

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
