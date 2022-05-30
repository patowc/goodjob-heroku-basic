from flask import Flask
from datetime import datetime
mi_super_duper_aplicacion = Flask(__name__)

@mi_super_duper_aplicacion.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>¡Hola Goodjob!</h1>
    <p>La hora actual es: {time}.</p>
    <hr>
    <p>Adios Goodjob :)</p>
    """.format(time=the_time)

@mi_super_duper_aplicacion.route('/secreto')
def homepage_secreto():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>¡Hola Goodjob (SUPERSECRETO)!</h1>
    <p>La hora actual es: {time}.</p>
    <hr>
    <p>Adios Goodjob :)</p>
    """.format(time=the_time)

if __name__ == '__main__':
    mi_super_duper_aplicacion.run(debug=True, use_reloader=True)

