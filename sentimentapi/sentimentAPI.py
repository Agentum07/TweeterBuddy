# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:21:26 2021

@author: njtj1
"""


from flask import Flask, request, jsonify
from flask_cors import CORS
import Model as model

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api', methods=['GET'])
def hello_world():
    
    d = {}
    d['Query'] = str(model.input(request.args['Query']))
    return jsonify(d);

if __name__ == '__main__':
    app.run()