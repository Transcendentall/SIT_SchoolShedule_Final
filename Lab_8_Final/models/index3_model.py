import pandas


def get_cabinet(conn):
    return pandas.read_sql(
        '''SELECT * FROM cabinets
''', conn)


def get_cabinet_found(conn, cabinet_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 cabinet_name AS Кабинет,
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 group_name AS Класс, 
 teacher_name AS Учитель
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE cabinet_id = :caid AND day_of_week_id = 1
 ORDER BY lesson_id
         ''', conn, params={"caid": cabinet_id})


def get_cabinet_found2(conn, cabinet_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 cabinet_name AS Кабинет,
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 group_name AS Класс, 
 teacher_name AS Учитель
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE cabinet_id = :caid AND day_of_week_id = 2
 ORDER BY lesson_id
         ''', conn, params={"caid": cabinet_id})

def get_cabinet_found3(conn, cabinet_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 cabinet_name AS Кабинет,
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 group_name AS Класс, 
 teacher_name AS Учитель
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE cabinet_id = :caid AND day_of_week_id = 3
 ORDER BY lesson_id
         ''', conn, params={"caid": cabinet_id})

def get_cabinet_found4(conn, cabinet_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 cabinet_name AS Кабинет,
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 group_name AS Класс, 
 teacher_name AS Учитель
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE cabinet_id = :caid AND day_of_week_id = 4
 ORDER BY lesson_id
         ''', conn, params={"caid": cabinet_id})

def get_cabinet_found5(conn, cabinet_id):
    # выбираем и выводим записи о том, какие книги брал читатель
    return pandas.read_sql('''
SELECT 
 cabinet_name AS Кабинет,
 lesson_id AS Номер_урока, 
 lesson_time AS Время_урока, 
 subject_name AS Предмет, 
 group_name AS Класс, 
 teacher_name AS Учитель
 FROM subjecthours
 JOIN groups USING (group_id)
 JOIN subjects USING (subject_id)
 JOIN teachers USING (teacher_id)
 JOIN dayshedule USING (subjecthours_id)
 JOIN daysofweek USING (day_of_week_id)
 JOIN lessons USING (lesson_id)
 JOIN cabinets USING (cabinet_id)
 WHERE cabinet_id = :caid AND day_of_week_id = 5
 ORDER BY lesson_id
         ''', conn, params={"caid": cabinet_id})


def get_new_cabinet(conn, new_cabinet):
    """
    Функция для обработки данных о новом читателе
    """
    cur = conn.cursor()

    cur.execute('''
INSERT INTO cabinet(cabinet_name) VALUES (:new_cabinet)
    ''', {"new_cabinet": new_cabinet})

    conn.commit()

    return cur.lastrowid


