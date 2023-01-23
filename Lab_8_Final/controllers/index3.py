from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index3_model import get_cabinet, get_cabinet_found, get_cabinet_found2, get_cabinet_found3, get_cabinet_found4, get_cabinet_found5, get_new_cabinet


@app.route('/index3', methods=['get'])
def index3():
    conn = get_db_connection()

    if request.values.get('cabinet'):
        cabinet_id = int(request.values.get('cabinet'))
        session['cabinet_id'] = cabinet_id
    elif request.values.get('new_cabinet'):
        new_cabinet = request.values.get('new_cabinet')
        session['cabinet_id'] = get_new_cabinet(conn, new_cabinet)
    elif request.values.get('return'):
        cabinet_found_id = int(request.values.get('return'))
        return_book(conn, cabinet_found_id)
    elif request.values.get('return'):
        cabinet_found_id2 = int(request.values.get('return'))
        return_book(conn, cabinet_found_id2)
    elif request.values.get('return'):
        cabinet_found_id3 = int(request.values.get('return'))
        return_book(conn, cabinet_found_id3)
    elif request.values.get('return'):
        cabinet_found_id4 = int(request.values.get('return'))
        return_book(conn, cabinet_found_id4)
    elif request.values.get('return'):
        cabinet_found_id5 = int(request.values.get('return'))
        return_book(conn, cabinet_found_id5)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        borrow_book(conn, book_id, session['cabinet_id'])
    else:
        session['cabinet_id'] = 1

    df_cabinet = get_cabinet(conn)
    df_cabinet_found = get_cabinet_found(conn, session['cabinet_id'])
    df_cabinet_found2 = get_cabinet_found2(conn, session['cabinet_id'])
    df_cabinet_found3 = get_cabinet_found3(conn, session['cabinet_id'])
    df_cabinet_found4 = get_cabinet_found4(conn, session['cabinet_id'])
    df_cabinet_found5 = get_cabinet_found5(conn, session['cabinet_id'])

    # выводим форму
    html = render_template(
        'index3.html',
        cabinet_id=session['cabinet_id'],
        combo_box=df_cabinet,
        cabinet_found=df_cabinet_found,
        cabinet_found2=df_cabinet_found2,
        cabinet_found3=df_cabinet_found3,
        cabinet_found4=df_cabinet_found4,
        cabinet_found5=df_cabinet_found5,
        len=len
    )
    return html
