#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:57:04 2019

@author: steve
"""

import easy_id as ei

from flask import Flask,json,request,render_template
app=Flask(__name__)

@app.route('/' ,methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        ist=request.form['input_string']
        easy=ei.easy_id(ist)
        return render_template('index.html',value=ist,gid=easy)
    else:
        return render_template('index.html')    

@app.route('/easyid/')
@app.route('/easyid/<some_value>')
def easyid(some_value=None):
    easy=ei.easy_id(some_value)
    return render_template('showid.html',value=some_value,gid=easy)


@app.route('/api/easyid/<some_value>')
def apieasyid(some_value):
    return json.jsonify(id=ei.easy_id(some_value))