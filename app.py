from flask import Flask, request, jsonify
import json
import pandas as pd
from politician import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    #Get data from Post request
    data =  request.json.get('Name')
    pred = get_recommendations(data)
    return jsonify({"Predictions": pred})
    #return pred.to_json()

if __name__ == "__main__":
   app.run(debug=True)
   
