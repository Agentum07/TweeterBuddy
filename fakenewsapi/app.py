# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:40:52 2021

@author: agent
"""

from flask import Flask, jsonify, request
import pickle
import pandas as pd
import string
from flask_cors import CORS

def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# routes
@app.route('/api', methods=['GET'])
def predict():
    # get data
    data = request.args['Query']
    lines2 = []
    lines2.append(data)
    df = pd.DataFrame({'text' : lines2}).astype(str)
    df['text'] = df['text'].apply(lambda x: x.lower())
    input_df = df.apply(punctuation_removal)
    
    result = {}
    
    # predictions
    result['Query'] = model.predict(input_df)[0]

    # return data
    return jsonify(result)

if __name__ == '__main__':
    app.run(port = 5000, debug = True, use_reloader = False)