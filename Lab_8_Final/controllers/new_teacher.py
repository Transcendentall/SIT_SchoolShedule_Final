from app import app
from flask import render_template


@app.route('/new_teacher', methods=['get'])
def new_teacher():
    html = render_template(
        'new_teacher.html',
    )
    return html