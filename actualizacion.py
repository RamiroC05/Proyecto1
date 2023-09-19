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

# Obtener el ID de la persona de los parámetros de la URL
form = cgi.FieldStorage()

id = form["id"].value
Nombre = form["name"].value
Apellido = form["surname"].value
DNI = int(form["dni"].value)
Domicilio = form["domicilio"].value 
Email = form["email"].value
Edad = int(form["edad"].value)
Genero = form["genero"].value
Cuil = int(form["cuil"].value)


cursor1.execute (f"UPDATE `proyecto`.`empleados` SET `Nombre` = '{Nombre}', `Apellido` = '{Apellido}', `DNI` = '{DNI}', `Domicilio` = '{Domicilio}', `Email` = '{Email}', `Edad` = '{Edad}', `Género` = '{Genero}', `Cuil` = '{Cuil}' WHERE (`ID_Empleado` = '{id}');")

conexion1.commit()

print(f"<h1 style='font-family: verdana; font-size: 400%; color: lightblue; text-align:center;'>LOS DATOS HAN SIDO MODIFICADOS</h1>")
print("<a href='proyecto1.py'>Volver a la pagina principal</a>")
conexion1.close()