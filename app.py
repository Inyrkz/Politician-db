from flask import Flask, request, jsonify
# import numpy as np
import json
import pandas as pd
from politician import get_recommendations

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    #Get data from Post request
    data =  request.json.get('Name')
    pred = get_recommendations(data)
    return pred.to_json()

if __name__ == "__main__":
   app.run(debug=True)
   