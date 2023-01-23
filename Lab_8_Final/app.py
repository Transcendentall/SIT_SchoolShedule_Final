# импорт объекта для создания приложения
from flask import Flask, session

# создание экземпляра объекта приложения
app = Flask(__name__)

# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# здесь необходимо указать все контроллеры страниц
# закомментировать еще не реализованные
import controllers.index1
import controllers.index2
import controllers.index3
import controllers.new_cabinet
import controllers.new_class
import controllers.new_subject
import controllers.new_teacher
