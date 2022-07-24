# If a user managed to submit the name <script>alert("bad")</script>,
# escaping causes it to be rendered as text, rather than running the script in the user’s browser.
#
# <name> in the route captures a value from the URL and passes it to the view function.

from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run()