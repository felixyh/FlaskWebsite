# use the methods argument of the route() decorator to handle different HTTP methods.

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

