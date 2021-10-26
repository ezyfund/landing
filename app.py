from flask import Flask, render_template, request,send_from_directory, jsonify, url_for
from flask import redirect

# from scripts import helper
import requests


import json

import time
import os
import pickle

from util.read_sheet import get_sheet
from util.read_sheet import insert_row

application = Flask(__name__)

@application.route('/home')
def home():    
    return render_template('index.html')


@application.route('/')
def index():    
    return render_template('index.html')

####################################################################
####################################################################
####################################################################


@application.route('/entrepreneur', methods = ['GET', 'POST'])
def entrepreneur():
    return render_template("index_entrepreneur.html")





@application.route('/entrepreneur_join', methods = ['POST'])
def entrepreneur_join():
    print("here")
    print(request)
    row = str(request.form['handle'])
    print("Handle is ",row)
    status=insert_row([row],"EntrepreneurHandles")
    if not status:
        render_template("index_entrepreneur.html")
    
    return render_template("thnx_entrepreneur.html")


@application.route('/thnx_entrepreneur', methods = ['GET', 'POST'])
def thnx_entrepreneur():
    return render_template("thnx_entrepreneur.html")



####################################################################
####################################################################
####################################################################

@application.route('/investor', methods = ['GET', 'POST'])
def investor():
    return render_template("index_investor.html")

@application.route('/investor_join', methods = ['POST'])
def investor_join():
    print(request)
    row = str(request.form['handle'])
    status=insert_row([row],"InvestorHandles")
    if not status:
        render_template("index_investor.html")
    
    return render_template("thnx_investor.html")



@application.route('/thnx_investor', methods = ['GET', 'POST'])
def thnx_investor():
    return render_template("thnx_investor.html")




if __name__ == "__main__":
    
    application.run(debug=True,port=8111)