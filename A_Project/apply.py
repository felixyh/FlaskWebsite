from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField
from wtforms.validators import email, length, input_required


app = Flask(__name__)
bootstrap = Bootstrap5(app)




