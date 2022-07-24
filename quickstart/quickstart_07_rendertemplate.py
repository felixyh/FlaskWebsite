from flask import Flask, render_template

app = Flask(__name__)

'''
Generating HTML from within Python is not fun, 
and actually pretty cumbersome 
because you have to do the HTML escaping on your own to keep the application secure.
Because of that Flask configures the Jinja2 templates engine for you automatically.
'''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
