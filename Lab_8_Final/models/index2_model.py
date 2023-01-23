import pandas


def get_teacher(conn):
    return pandas.read_sql(
        '''SELECT * FROM teachers
''', conn)


def get_teacher_found(conn, teacher_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 teacher_name AS Учитель, 
 lesson_id AS Номер_урока, 
 group_name AS Класс, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE teacher_id = :teid AND day_of_week_id = 1
 ORDER BY lesson_id
         ''', conn, params={"teid": teacher_id})


def get_teacher_found2(conn, teacher_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 teacher_name AS Учитель, 
 lesson_id AS Номер_урока, 
 group_name AS Класс, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE teacher_id = :teid AND day_of_week_id = 2
 ORDER BY lesson_id
         ''', conn, params={"teid": teacher_id})

def get_teacher_found3(conn, teacher_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 teacher_name AS Учитель, 
 lesson_id AS Номер_урока, 
 group_name AS Класс, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE teacher_id = :teid AND day_of_week_id = 3
 ORDER BY lesson_id
         ''', conn, params={"teid": teacher_id})

def get_teacher_found4(conn, teacher_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 teacher_name AS Учитель, 
 lesson_id AS Номер_урока, 
 group_name AS Класс, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE teacher_id = :teid AND day_of_week_id = 4
 ORDER BY lesson_id
         ''', conn, params={"teid": teacher_id})

def get_teacher_found5(conn, teacher_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 teacher_name AS Учитель, 
 lesson_id AS Номер_урока, 
 group_name AS Класс, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 cabinet_name AS Кабинет
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE teacher_id = :teid AND day_of_week_id = 5
 ORDER BY lesson_id
         ''', conn, params={"teid": teacher_id})


def get_new_teacher(conn, new_teacher):
    """
    Функция для обработки данных о новом читателе
    """
    cur = conn.cursor()

    cur.execute('''
INSERT INTO teacher(teacher_name) VALUES (:new_teacher)
    ''', {"new_teacher": new_teacher})

    conn.commit()

    return cur.lastrowid

