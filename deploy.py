from flask import Flask, request, jsonify
import json
from politician import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        #Get data from Post request
        data =  request.json.get('Name')
        #fit data into get recommendation function
        pred = get_recommendations(data)
    return jsonify({"Predictions": pred})
    #return pred.to_json()

# @app.route('/', methods=['GET'])
# def pred():
#     return "Get method dey work o"
#     #return pred.to_json()

if __name__ == "__main__":
   app.run(debug=True)
   