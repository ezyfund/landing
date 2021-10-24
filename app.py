from flask import Flask, render_template, request,send_from_directory, jsonify, url_for
from flask import redirect

# from scripts import helper
import requests


import json

import time
import os
import pickle

application = Flask(__name__)

@application.route('/')
def index():    
    return render_template('index.html')




if __name__ == "__main__":
    
    application.run(debug=True,port=8111)