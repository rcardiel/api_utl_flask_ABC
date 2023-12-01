
from flask import Flask,jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion=MySQL(app)

#""" listar totodos los alumnos """

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try:
        cursor=conexion.connection.cursor()
        sql="select * from alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        listAlum=[]
        for fila in datos:
            alum={'matricula':fila[0],'nombre':fila[1],'apaterno':fila[2],'amaterno':fila[3],'correo':fila[4]}
            listAlum.append(alum)

        return jsonify({'cursos':listAlum, 'mensaje':"lista de alumnos"})
    except Exception as ex:
        return jsonify({'mensaje':'error'})

#""" consultar por matricula """
@app.route('/alumnos/<mat>',methods=['GET'])
def leer_alumno(mat):
    try:
     cursor=conexion.connection.cursor()
     sql="select * from alumnos where matricula= '{0}'".format(mat)
     cursor.execute(sql)
     datos=cursor.fetchone()
     if datos != None:
           alum={'matricula':datos[0],'nombre':datos[1],'apaterno':datos[2],'amaterno':datos[3],'correo':datos[4]}
           return jsonify({'alumno':alum, 'mensaje':'Alumno encontrado'})
     else:
        return jsonify({'mensaje': 'Alumno no encontrado.'}) 
    except Exception as ex:
        return jsonify({'mensaje':'error'})


@app.route('/alumnos',methods=['POST'])
def registrar_alumno():
    try:
        #print(request.json)
        return jsonify({'mensaje':'curso registrado'})
    except Exception as ex:
        return jsonify({'mensaje':'error'})



def pagina_no_encontrada(error):
    return "<h1> pagina no existe</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()