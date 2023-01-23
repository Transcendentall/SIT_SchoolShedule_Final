import pandas


def get_group(conn):
    return pandas.read_sql(
        '''SELECT * FROM groups
''', conn)


def get_group_found(conn, group_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 group_name AS Класс, 
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 teacher_name AS Учитель, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE group_id = :grid AND day_of_week_id = 1
 ORDER BY lesson_id
         ''', conn, params={"grid": group_id})


def get_group_found2(conn, group_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 group_name AS Класс, 
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 teacher_name AS Учитель, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE group_id = :grid AND day_of_week_id = 2
 ORDER BY lesson_id
         ''', conn, params={"grid": group_id})


def get_group_found3(conn, group_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 group_name AS Класс, 
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 teacher_name AS Учитель, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE group_id = :grid AND day_of_week_id = 3
 ORDER BY lesson_id
         ''', conn, params={"grid": group_id})


def get_group_found4(conn, group_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 group_name AS Класс, 
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 teacher_name AS Учитель, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE group_id = :grid AND day_of_week_id = 4
 ORDER BY lesson_id
         ''', conn, params={"grid": group_id})


def get_group_found5(conn, group_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 group_name AS Класс, 
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 teacher_name AS Учитель, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE group_id = :grid AND day_of_week_id = 5
 ORDER BY lesson_id
         ''', conn, params={"grid": group_id})


def get_new_class(conn, new_class):
    cur = conn.cursor()
    cur.execute('''
INSERT INTO groups(group_name) VALUES (:new_class)
    ''', {"new_class": new_class})
    conn.commit()
    return cur.lastrowid

def get_new_cabinet(conn, new_cabinet):
    cur = conn.cursor()
    cur.execute('''
INSERT INTO cabinets(cabinet_name) VALUES (:new_cabinet)
    ''', {"new_cabinet": new_cabinet})
    conn.commit()
    return cur.lastrowid

def get_new_subject(conn, new_subject):
    cur = conn.cursor()
    cur.execute('''
INSERT INTO subjects(subject_name) VALUES (:new_subject)
    ''', {"new_subject": new_subject})
    conn.commit()
    return cur.lastrowid

def get_new_teacher(conn, new_teacher_name, new_teacher_subject):
    cur = conn.cursor()
    cur.execute('''
INSERT INTO teachers(teacher_name, subject_id) VALUES (:new_teacher_name, :new_teacher_subject)
    ''', {"new_teacher_name": new_teacher_name, "new_teacher_subject": new_teacher_subject})
    conn.commit()
    return cur.lastrowid

