from flask import Flask, request, jsonify
import pickle
import numpy as np

# create a Flask app
app = Flask(__name__)

# define the route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # load the trained model from the pickle file
    with open('linear_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # get the input data from the request
    data = request.get_json()

    # convert the input data into a numpy array
    X = np.array([[data['yearsExperience']]])

    # make a prediction using the model
    prediction = model.predict(X)


    # create a response object
    response = {
        
        'prediction': prediction[0]
    }

    # return the response as a JSON object
    return jsonify(response)

# start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
