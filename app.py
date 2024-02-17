"""
A simple dog flask app
"""
from flask import Flask, render_template, request
import gbmodel
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/all_breeds', methods=['GET'])
def all_breeds():
    response = gbmodel.get_model().breeds()
    if response['status'] == 'success':
        breed_names = list(response['message'].keys())
        return render_template('all_breeds.html', breeds=breed_names)
    else:
        return render_template('all_breeds.html', breeds=[], error="No dog breeds were found")

@app.route('/breed_input', methods=['GET'])
def breed_input():
    return render_template('breed_input.html')

@app.route('/show_breed', methods=['POST'])
def show_breed():
    breed = request.form['breed']
    response = gbmodel.get_model().a_breed(breed)
    if response['status'] == 'success':
        return render_template('breed_display.html', breed_name=breed, images=response['message'])
    else:
        return render_template('breed_display.html', breed_name=breed, images=[], error=f"No images were found for the breed '{breed}'")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
