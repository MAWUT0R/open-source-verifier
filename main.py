# import main flask class, render_template, request object
from flask import Flask, render_template, request, redirect
from utils import *

# Create the Flask app
app = Flask(__name__)

# Define route for home page
@app.route('/')
def hello():
    return render_template('index.html')

# Defines route for verification
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    # handle the POST request
    if request.method == 'POST':
        app_id = request.form.get('app_id')
        github_url = str(request.form.get('github_url'))

        response = verify_source(app_id, github_url)
        return render_template('verify.html', data=response)

    # otherwise handle the GET request which redirects to home page
    return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
