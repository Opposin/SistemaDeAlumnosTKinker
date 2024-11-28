import mysql.connector

import Configuracion
from Configuracion import *

import tkinter as tk
from tkinter import messagebox



class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            if Configuracion.VerificarConfiguracion() == True and verificarVacio() == False:    
                configConexion = Configuracion.LeerConfiguracion()
                conexion = mysql.connector.connect(user = configConexion[0], password = configConexion[1], host = configConexion[2], database = configConexion[3], raise_on_warnings = True)
                cursor = conexion.cursor()
                tabla = "alumnos"
                 
                cursor.execute(f"SHOW TABLES LIKE '{tabla}'")
                resultado = cursor.fetchone()
                
                if resultado == None:
                    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabla} (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(25), apellido VARCHAR(25), dni VARCHAR(25), fecha_nacimiento DATE, telefono VARCHAR(25), direccion VARCHAR(25), edad INT)")
                
                return conexion
       
        except mysql.connector.Error as error:
            print(f"Error al conectar con la base de datos, error {error}")
            messagebox.showerror("Error", "Error al conectar con la base de datos, verifique la configuracion")
            
            
    def CerrarConexion(conexion):
        try:
            conexion.close()
            print("conexion cerrada")
            
        except mysql.connector.Error as error:
            print(f"Error al cerrar la conexion, error {error}")
            messagebox.showerror("Error", "Error al cerrar la conexion, verifique la configuracion")
    