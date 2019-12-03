'''flask restful api'''
import json
from flask import Flask, request, jsonify
from flask_restful import Api
from politician import get_recommendations

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def predict():
    '''function under post request'''
    #Get data from Post request
    data = request.json.get('Name')
    #fit input data into get recommendation function
    pred = get_recommendations(data)
    return jsonify({"Predictions": pred})
    #return pred.to_json()


if __name__ == "__main__":
    app.run(debug=True)
   