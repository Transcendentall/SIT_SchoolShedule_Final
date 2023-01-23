from app import app
from flask import render_template


@app.route('/new_subject', methods=['get'])
def new_subject():
    html = render_template(
        'new_subject.html',
    )
    return html