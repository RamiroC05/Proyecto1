print("Content-Type: text/html")
print()
print("<html>")
print ("<head>")
print("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9' crossorigin='anonymous'>")
print("<script src='https://kit.fontawesome.com/4b7878dea0.js' crossorigin='anonymous'></script>")
print ("<title>TABLAS DE MYSQL</title>") 

import cgi
import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PROGRAMACION2023",
    database="proyecto"
)

cursor1 = conexion1.cursor()

form = cgi.FieldStorage()
id_persona = form.getvalue("id")


cursor1.execute(f"delete FROM Empleados WHERE `ID_Empleado` = '{id_persona}'")
conexion1.commit()

print("<div class='alert alert-success'>USUARIO ELIMINADO CORRECTAMENTE</div>")
print("<a href='proyecto1.py'>Volver a la página principal</a>")

conexion1.close()




