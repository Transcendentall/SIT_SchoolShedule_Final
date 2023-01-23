from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index2_model import get_teacher, get_teacher_found, get_teacher_found2, get_teacher_found3, get_teacher_found4, get_teacher_found5, get_new_teacher


@app.route('/index2', methods=['get'])
def index2():
    conn = get_db_connection()

    if request.values.get('teacher'):
        teacher_id = int(request.values.get('teacher'))
        session['teacher_id'] = teacher_id
    elif request.values.get('new_teacher'):
        new_teacher = request.values.get('new_teacher')
        session['teacher_id'] = get_new_teacher(conn, new_teacher)
    elif request.values.get('return'):
        teacher_found_id = int(request.values.get('return'))
        return_book(conn, teacher_found_id)
    elif request.values.get('return'):
        teacher_found_id2 = int(request.values.get('return'))
        return_book(conn, teacher_found_id2)
    elif request.values.get('return'):
        teacher_found_id3 = int(request.values.get('return'))
        return_book(conn, teacher_found_id3)
    elif request.values.get('return'):
        teacher_found_id4 = int(request.values.get('return'))
        return_book(conn, teacher_found_id4)
    elif request.values.get('return'):
        teacher_found_id5 = int(request.values.get('return'))
        return_book(conn, teacher_found_id5)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        borrow_book(conn, book_id, session['teacher_id'])
    else:
        session['teacher_id'] = 1

    df_teacher = get_teacher(conn)
    df_teacher_found = get_teacher_found(conn, session['teacher_id'])
    df_teacher_found2 = get_teacher_found2(conn, session['teacher_id'])
    df_teacher_found3 = get_teacher_found3(conn, session['teacher_id'])
    df_teacher_found4 = get_teacher_found4(conn, session['teacher_id'])
    df_teacher_found5 = get_teacher_found5(conn, session['teacher_id'])

    # выводим форму
    html = render_template(
        'index2.html',
        teacher_id=session['teacher_id'],
        combo_box=df_teacher,
        teacher_found=df_teacher_found,
        teacher_found2=df_teacher_found2,
        teacher_found3=df_teacher_found3,
        teacher_found4=df_teacher_found4,
        teacher_found5=df_teacher_found5,
        len=len
    )
    return html
