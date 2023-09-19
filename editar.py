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
id_persona = form.getvalue("id")
nombre = form.getvalue("name")
apellido = form.getvalue("surname")
dni = form.getvalue("dni")
domicilio = form.getvalue("domicilio")
email = form.getvalue("email")
edad = form.getvalue("edad")
genero = form.getvalue("genero")
cuil = form.getvalue("cuil")

print(f"<h1 style='font-family: verdana; font-size: 400%; color: lightblue; text-align:center;'>ID de la persona seleccionada: {id_persona}</h1>")


print("""<div class='container-fluid row justify-content-center'>
        <div class='col-6'>
      <h3 class='text-center text-secondary'>DATOS A MODIFICAR DEL EMPLEADO</h3>
            <form method='get' action='actualizacion.py'>""")
print("""
                <div class="mb-3">
                    ID""")
print( f"<input type='text' class='form-control' name='id' value='{id_persona}'disabled>")
print( f"<input type='hidden' name='id' value={id_persona}>")
print("""

                <div class="mb-3">
                    Nombre""")

print(f"<input type='text' class='form-control' name='name' value='{nombre}'>")
print("""
                </div>
                  
                <div class="mb-3">
                    Apellido""")
print(f"<input type='text' class='form-control' name='surname' value='{apellido}'>")
print("""
                </div>
                
                <div class="mb-3">
                    DNI""")
print(f"<input type='number' class='form-control' name='dni' value='{dni}'>")
print("""
                </div>
                
                <div class="mb-3">
                Domicilio""")

print(f"<input type='text' class='form-control' name='domicilio' value='{domicilio}'>")
print("""
                </div>                
                
                <div class="mb-3">
                    Email""")
print(f"<input type='text' class='form-control' name='email' value='{email}'>")
print("""
                </div>
                
                <div class="mb-3">
                    Edad""")
print(f"<input type='number' class='form-control' name='edad' value='{edad}'>")
print("""
                </div>
                
                <div class="mb-3">
                    Género""")
print(f"<input type='text' class='form-control' name='genero' value='{genero}'>")
print("""
                </div>
                
                <div class="mb-3">
                    Cuil""")
print(f"<input type='number' class='form-control' name='cuil' value='{cuil}'>")
print("""
                </div>
                
                <button type='submit' class='btn btn-primary'>MODIFICAR</button> 
                
                </form>
            </form>
      </div>
      </div>""")



