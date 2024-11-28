from Conexion import *



class CAlumnos:
    def MostrarAlumnos(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos")
            resultado = cursor.fetchall()
            for result in resultado:
                print(result)
            conexion.commit()
            cursor.close()
            CConexion.CerrarConexion(conexion)
            return resultado
            
        
        except mysql.connector.Error as error:
            print(f"Error al mostrar alumnos, error {error}")
            
        
    
    def IngresarAlumno(conexion, nombre, apellido, dni, fecha_nacimiento, telefono, direccion, edad):
        try:
            cursor = conexion.cursor()
            
            tabla = "alumnos"
            
            """cursor.execute(f"SHOW TABLES LIKE '{tabla}'")
            resultado = cursor.fetchone()
            
            if resultado == None:
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabla} (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(25), apellido VARCHAR(25), dni VARCHAR(25), fecha_nacimiento VARCHAR(25), telefono VARCHAR(25), direccion VARCHAR(25))")"""
            
            cursor.execute(f"INSERT INTO {tabla} (nombre, apellido, dni, fecha_nacimiento, telefono, direccion, edad) VALUES ('{nombre}', '{apellido}', '{dni}', '{fecha_nacimiento}', '{telefono}', '{direccion}', '{edad}')")
            conexion.commit()
            print(cursor.rowcount,"alumno ingresado")
            
            
            cursor.close()
            CConexion.CerrarConexion(conexion)
        
        except mysql.connector.Error as error:
            print(f"Error al ingresar alumno, error {error}")
    
    def ActualizarAlumno(conexion, id, nombre, apellido, dni, fecha_nacimiento, telefono, direccion, edad):
        try:
            
            cursor = conexion.cursor()
            
            tabla = "alumnos"
            
            cursor.execute(f"UPDATE {tabla} SET nombre = '{nombre}', apellido = '{apellido}', dni = '{dni}', fecha_nacimiento = '{fecha_nacimiento}', telefono = '{telefono}', direccion = '{direccion}', edad = {edad} WHERE id = {id}")
            conexion.commit()
            print(cursor.rowcount,"alumno modificado")
            
            
            cursor.close()
            CConexion.CerrarConexion(conexion)
        
        except mysql.connector.Error as error:
            print(f"Error al modificar alumno, error {error}")
            
            
    def EliminarAlumno(conexion, id):
        try:
            
            cursor = conexion.cursor()
            
            tabla = "alumnos"
            
            cursor.execute(f"DELETE FROM {tabla} WHERE id = {id}")
            conexion.commit()
            print(cursor.rowcount,"alumno eliminado")
            
            
            cursor.close()
            CConexion.CerrarConexion(conexion)
            
        except mysql.connector.Error as error:
            print(f"Error al eliminar alumno, error {error}")