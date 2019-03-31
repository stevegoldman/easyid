#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:57:04 2019

@author: steve
"""

import easy_id as ei
from flask import Flask,json,request,render_template
from werkzeug.exceptions import BadRequest
app=Flask(__name__)

@app.errorhandler(400)
def handle_invalid_usage(ex):
    response = json.jsonify(error=ex.description)
    response.status_code = 400
    return response        

@app.route('/' ,methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        ist=request.form['input_string']
        easy=ei.easy_id(ist)
        return render_template('index.html',value=ist,gid=easy)
    else:
        return render_template('index.html')    


@app.route('/api/easyid/<some_value>')
def apieasyid(some_value):
    return json.jsonify(easyid=ei.easy_id(some_value),
                         input_string=some_value)

@app.route('/api/easyids/',methods=['POST'])
def api_multiple():
    if request.get_json():
        los=request.get_json()
        if type(los)==type([]):
            ok=True
            for s in los:
                if type(s)!=type('hello'):
                    ok=False
                    break
            if ok:
                return multiple_ids(los)
        else:
            
            raise BadRequest('JSON payload must be array of strings.')
    
    else:
        raise BadRequest('API requires JSON POST data, Content-Type: application/json.')
            


def multiple_ids(python_list_of_strings):
    ret=[]
    for s in python_list_of_strings:
        r={}
        r['input_string']=s
        r['easyid']=ei.easy_id(s)
        ret.append(r)
    return json.jsonify(ret)    



