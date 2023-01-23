from app import app
from flask import render_template


@app.route('/new_class', methods=['get'])
def new_class():
    html = render_template(
        'new_class.html',
    )
    return html