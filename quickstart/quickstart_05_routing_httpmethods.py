# use the methods argument of the route() decorator to handle different HTTP methods.

from flask import Flask, request

app = Flask(__name__)

# Method-1:By default, a route only answers to GET requests.
# You can use the methods argument of the route() decorator to handle different HTTP methods.


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


# Method-2: separate views for different methods into different functions.
# Flask provides a shortcut for decorating such routes with get(), post(), etc. for each common HTTP method.
@app.get('/login')
def get_login():
    return show_the_login_form()


@app.post('/login')
def post_login():
    return do_log_login()
