from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index1_model import get_group, get_group_found, get_group_found2, get_group_found3, get_group_found4, get_group_found5, get_new_class, get_new_cabinet, get_new_subject, get_new_teacher


@app.route('/index1', methods=['get'])
def index1():
    conn = get_db_connection()

    if request.values.get('group'):
        group_id = int(request.values.get('group'))
        session['group_id'] = group_id
    elif request.values.get('new_class'):
        new_class = request.values.get('new_class')
        session['group_id'] = get_new_class(conn, new_class)
    elif request.values.get('new_subject'):
        new_subject = request.values.get('new_subject')
        session['subject_id'] = get_new_subject(conn, new_subject)
    elif request.values.get('new_teacher'):
        new_teacher = request.values.get('new_teacher')
        session['teacher_id'] = get_new_teacher(conn, new_teacher)
    elif request.values.get('new_cabinet'):
        new_cabinet = request.values.get('new_cabinet')
        session['cabinet_id'] = get_new_cabinet(conn, new_cabinet)
    elif request.values.get('return'):
        group_found_id = int(request.values.get('return'))
        return_book(conn, group_found_id)
    elif request.values.get('return'):
        group_found_id2 = int(request.values.get('return'))
        return_book(conn, group_found_id2)
    elif request.values.get('return'):
        group_found_id3 = int(request.values.get('return'))
        return_book(conn, group_found_id3)
    elif request.values.get('return'):
        group_found_id4 = int(request.values.get('return'))
        return_book(conn, group_found_id4)
    elif request.values.get('return'):
        group_found_id5 = int(request.values.get('return'))
        return_book(conn, group_found_id5)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        borrow_book(conn, book_id, session['group_id'])
    else:
        session['group_id'] = 1

    df_group = get_group(conn)
    df_group_found = get_group_found(conn, session['group_id'])
    df_group_found2 = get_group_found2(conn, session['group_id'])
    df_group_found3 = get_group_found3(conn, session['group_id'])
    df_group_found4 = get_group_found4(conn, session['group_id'])
    df_group_found5 = get_group_found5(conn, session['group_id'])

    # выводим форму
    html = render_template(
        'index1.html',
        group_id=session['group_id'],
        combo_box=df_group,
        group_found=df_group_found,
        group_found2=df_group_found2,
        group_found3=df_group_found3,
        group_found4=df_group_found4,
        group_found5=df_group_found5,
        len=len
    )
    return html
