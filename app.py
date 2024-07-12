from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask import Flask
 

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Nombre de usuario de MySQL
app.config['MYSQL_PASSWORD'] = '11Deseptiembre'  # Contraseña de MySQL
app.config['MYSQL_DB'] = 'tour_arg_db'  # Nombre de la base de datos

# Inicialización de Flask-MySQLdb
mysql = MySQL(app)
CORS(app,resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

  

@app.route('/',methods=['GET'])
  
def index():
    try:
        conn = mysql.connection   
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservas")
        reservas = cursor.fetchall()
        cursor.close()
        return render_template('Reservas/index.html', reservas =reservas)
    except Exception as e:
        return str(e)   
  
@app.route('/store', methods=['POST'])
def storage():
    try:
        Id=request.form['txtId']
        Nombre = request.form['txtNombre']
        Email = request.form['txtEmail']
        Mensaje = request.form['txtMensaje']
        
        conn = mysql.connection  # Obtener la conexión a la base de datos
        cursor = conn.cursor()
        sql = "INSERT INTO reservas(Id,Nombre,Email, Mensaje) VALUES (%s,%s, %s, %s)"
        cursor.execute(sql, (Id,Nombre, Email, Mensaje))  # Pasar los datos como una tupla
        conn.commit()
        cursor.close()
        
        return redirect('/')  # Redirigir a la página principal después de almacenar
    except Exception as e:
        return str(e)  # Manejo básico de errores para propósitos de depuración

# Ruta para mostrar formulario de edición de reserva
@app.route('/delete/<int:Id> ',methods=['DELETE'])
def delete(id):
    try:
        sql=f"DELETE FROM reservas WHERE id={id}"
        conn = mysql.connection  # Obtener la conexión a la base de datos
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
         
        
        return redirect('/')  # Redirigir a la página principal después de eliminar
    except Exception as e:
        return str(e)
    
@app.route('/create' )
def create():
    return render_template('Reservas/create.html'  )

@app.route('/edit/<int:id>',methods=['GET'] )
def edit(id):
    try:
        sql=f"SELECT FROM reservas WHERE id={id}"
        conn = mysql.connection  # Obtener la conexión a la base de datos
        cursor = conn.cursor()
        reservas=cursor.fetchone()
        cursor.execute(sql)
        conn.commit()
         
        
        return render_template('Reservas/edit.html', reservas= reservas)  # Redirigir a la página principal después de eliminar
    except Exception as e:
        return str(e)

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        Nombre = request.form['txtNombre']
        Email = request.form['txtEmail']
        Mensaje = request.form['txtMensaje']
        
        conn = mysql.connection  # Obtener la conexión a la base de datos
        cursor = conn.cursor()
        sql = "UPDATE reservas SET nombre=%s, email=%s, mensaje=%s WHERE id=%s"
        cursor.execute(sql, (Nombre, Email, Mensaje, id))  # Pasar los datos como una tupla
        conn.commit()
        cursor.close()
        
        return redirect('/')  # Redirigir a la página principal después de actualizar
    except Exception as e:
        return str(e)  # Manejo básico de errores para propósitos de depuración

# Ruta para eliminar reserva
  # Manejo básico de errores para propósitos de depuración

# Ruta para consultar todas las reservas (solo para propósitos de prueba)
@app.route('/consultar',methods=['PUT'])
def consultar():
    try:
        conn = mysql.connection  # Obtener la conexión a la base de datos
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservas")
        reservas = cursor.fetchall()
        cursor.close()
        
        return str(reservas)  # Devolver los resultados como una cadena (solo para propósitos de prueba)
    except Exception as e:
        return str(e)  # Manejo básico de errores para propósitos de depuración

if __name__ == '__main__':
    app.run(debug=True)
