from app import app
from flask import render_template


@app.route('/new_cabinet', methods=['get'])
def new_cabinet():
    html = render_template(
        'new_cabinet.html',
    )
    return html