import cgi
import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PROGRAMACION2023",
    database="proyecto"
)

cursor1 = conexion1.cursor()

cursor1.execute("SELECT * FROM Empleados")


print("Content-Type: text/html")
print()
print("<html>")
print ("<head>")
print("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9' crossorigin='anonymous'>")
print("<script src='https://kit.fontawesome.com/4b7878dea0.js' crossorigin='anonymous'></script>")
print ("<title> TABLAS DE MYSQL</title>") 




print ("""<body>
        <h1 style='font-family: verdana; font-size: 300%; color: lightblue; text-align:center;'>Tabla de empleados de GesEd.</h1>
        <h1 style='color: black; font-size: 200%; text-align:center;'>Con este sitio web podrás realizar ABM de la tabla de empleados</h1>

       
       <div class='conteiner-fluid row'>
            <form method='get' class= 'col-4 p-3'  >
                <br/>
                <br/>
                <br/>
                <h3 class='text-center text-secondary'>DATOS A INGRESAR DEL EMPLEADO</h3>
                <form>
                <div class="mb-3">
                    Nombre
                    <input type='text' class='form-control' name='name'>
                </div>
                  
                <div class="mb-3">
                    Apellido
                    <input type='text' class='form-control' name='surname'>
                </div>
                
                <div class="mb-3">
                    DNI
                    <input type='number' class='form-control' name='dni'>
                </div>
                
                <div class="mb-3">
                Domicilio
                    <input type='text' class='form-control' name='domicilio'>
                </div>                
                
                <div class="mb-3">
                    Email
                    <input type='text' class='form-control' name='email'>
                </div>
                
                <div class="mb-3">
                    Edad
                    <input type='number' class='form-control' name='edad'>
                </div>
                
                <div class="mb-3">
                    Género
                    <input type='text' class='form-control' name='genero'>
                </div>
                
                <div class="mb-3">
                    Cuil
                    <input type='number' class='form-control' name='cuil'>
                </div>
                
                <button type='submit' class='btn btn-primary'>Registrar</button>
                <input type='button' value='Actualizar' onclick='document.location.reload();'
                </form>
                
            </form>
            <div class='col-8 p-4'>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <table class='table'>
                <thead class= 'bg-info'>
                    <tr>
                        <th scope='col'>ID</th>
                        <th scope='col'>Nombre</th>
                        <th scope='col'>Apellido</th>
                        <th scope='col'>DNI</th>
                        <th scope='col'>Domicilio</th>
                        <th scope='col'>Email</th>
                        <th scope='col'>Edad</th>
                        <th scope='col'>Género</th>
                        <th scope='col'>Cuil</th>
                        <th scope='col'></th>
                    </tr>
                </thead>
                <tbody>""") 


for fila in cursor1:
    print("<tr>")
    for dato in fila:
        print(f"<td>{dato}</td>")
    print("<td>")
    print(f"<a href='editar.py?id={fila[0]}&name={fila[1]}&surname={fila[2]}&dni={fila[3]}&domicilio={fila[4]}&email={fila[5]}&edad={fila[6]}&genero={fila[7]}&cuil={fila[8]}' class='btn btn-small btn-warning'><i class='fa-solid fa-pen-to-square'></i></a>")
    print(f"<a href='eliminar.py?id={fila[0]}' class='btn btn-small btn-danger'><i class='fa-solid fa-trash'></i></a>")
    print("</td>")
    print("</tr>")


print("""

                </tbody>
                </table>    
       
            </div>

       </div>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js' integrity='sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm' crossorigin='anonymous'></script>
    </body>""") 



form = cgi.FieldStorage()

if "name" in form and "surname" in form and "dni" in form and "domicilio" in form and "email" in form and "edad" in form and "genero" in form and "cuil" in form:
    
    Nombre = form["name"].value
    Apellido = form["surname"].value
    DNI = int(form["dni"].value)
    Domicilio = form["domicilio"].value 
    Email = form["email"].value
    Edad = int(form["edad"].value)
    Genero = form["genero"].value
    Cuil = int(form["cuil"].value)

    cursor1.execute ("INSERT INTO Empleados(Nombre,Apellido,Dni,Domicilio,Email,Edad,Género,Cuil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (Nombre, Apellido, DNI, Domicilio, Email, Edad, Genero, Cuil))
  
    conexion1.commit()


    print ("<div class='alert alert-sucess'>USUARIO REGISTRADO CORRECTAMENTE</div>")
    

else:
    print ("<div class='alert alert-warning'>DEBE RELLENAR TODOS LOS CAMPOS</div>")

conexion1.close()

