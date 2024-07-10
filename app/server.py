from flask import Flask, jsonify, render_template, request
from create_ae import create_ae
from delete_ae import delete_ae
from retrive_ae import retrive_ae
from update_ae import update_ae
from config import *

app = Flask(__name__)

#render the index page (front-end)
@app.route('/')
def index():
    return render_template('index.html')

#create AE route
@app.route('/create_ae', methods=['POST'])
def create_ae_route():
    response = create_ae()  #call the create_ae function and store the response
    if response is not None:
        return jsonify(response), response.get("status", 200)  #return the actual response from the function
    else:
        return jsonify({"message": "Failed to create AE"}), 500

#delete AE route
@app.route('/delete_ae', methods=['DELETE'])
def delete_ae_route():
    response = delete_ae()  #call the delete_ae function and store the response
    if response is not None:
        return jsonify(response), response.get("status", 200)  #return the actual response from the function
    else:
        return jsonify({"message": "Failed to delete AE"}), 500

#retrieve AE route
@app.route('/retrive_ae', methods=['GET'])
def retrieve_ae_route():
    response = retrive_ae()  #call the retrieve_ae function and store the response
    if response is not None:
        return jsonify(response), response.get("status", 200)  #return the actual response from the function
    else:
        return jsonify({"message": "Failed to retrieve AE"}), 500

#update AE route
@app.route('/update_ae', methods=['PUT'])
def update_ae_route():
    response = update_ae()  #call the update_ae function and store the response
    if response is not None:
        return jsonify(response), response.get("status", 200)  #return the actual response from the function
    else:
        return jsonify({"message": "Failed to update AE"}), 500

if __name__ == "__main__":
    app.run(debug=True)

