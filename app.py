'''flask restful api'''
#importing some libraries
import json
from flask import Flask, request, jsonify
from flask_restful import Api
import politician
#from politician import get_recommendations
import pickle

#load pickled model i.e model pkl
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def predict():
    '''function under post request'''
    #Get data from Post request
    data = request.json.get('Name')
    #fit input data into get recommendation function
    pred = model(data)
    return jsonify({"Predictions": pred})
    #return pred.to_json()


if __name__ == "__main__":
    app.run(debug=True)
   