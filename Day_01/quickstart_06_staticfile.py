from flask import url_for

'''
To generate URLs for static files, use the special 'static' endpoint name
The file has to be stored on the filesystem as static/style.css.
'''

url_for('static', filename='style.css')