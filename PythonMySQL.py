import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from tkcalendar import DateEntry

from Alumnos import *

from Conexion import * 

from Verificaciones import *



class FormularioClientes:
    
    global base 
    base = None
    
    global groupBox
    groupBox = None
    
    global textBoxNombre
    textBoxNombre = None
    
    global textBoxApellido
    textBoxApellido = None
    
    global textBoxDNI
    textBoxDNI = None
    
    global PickerFechaNacimiento
    textBoxFechaNacimiento = None
    
    global textBoxTelefono
    textBoxTelefono = None
    
    global textBoxDireccion   
    textBoxDireccion = None
    
    global tree
    tree = None
        
def Formulario():
    
    global base
    global groupBox
    global textBoxNombre
    global textBoxApellido
    global textBoxDNI
    global PickerFechaNacimiento
    global textBoxTelefono
    global textBoxDireccion
    global tree
    

    try:
        base = Tk()
        base.geometry("1535x720")
        base.title("Formulario Alumnos")

        groupBox = LabelFrame(base, text="Datos del Alumno",  padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10, sticky="N")
        
        labelNombre = Label(groupBox, text="Nombre del alumno").grid(row=0, column=0, padx=5, pady=5)
        textBoxNombre = Entry(groupBox)
        textBoxNombre.grid(row=0, column=1, padx=5, pady=5)
        
        
        labelApellido = Label(groupBox, text="Apellido del alumno").grid(row=1, column=0, padx=5, pady=5)
        textBoxApellido = Entry(groupBox)
        textBoxApellido.grid(row=1, column=1, padx=5, pady=5)
        
        
        labelDNI = Label(groupBox, text="DNI del alumno").grid(row=2, column=0, padx=5, pady=5)
        textBoxDNI = Entry(groupBox)
        textBoxDNI.grid(row=2, column=1, padx=5, pady=5)
        
        
        labelFechaNacimiento = Label(groupBox, text="Fecha de nacimiento del alumno").grid(row=3, column=0, padx=5, pady=5)
        PickerFechaNacimiento = DateEntry(groupBox, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='yyyy/mm/dd')
        PickerFechaNacimiento.grid(row=3, column=1, padx=5, pady=5)
          
          
        labelTelefono = Label(groupBox, text="Telefono del alumno").grid(row=4, column=0, padx=5, pady=5)
        textBoxTelefono = Entry(groupBox)
        textBoxTelefono.grid(row=4, column=1, padx=5, pady=5)
        
        
        labelDireccion = Label(groupBox, text="Direccion del alumno").grid(row=5, column=0, padx=5, pady=5)
        textBoxDireccion = Entry(groupBox)
        textBoxDireccion.grid(row=5, column=1, padx=5, pady=5)
        
        labelEdad = Label(groupBox, text="Edad" , height=0).grid(row=6, column=0)
        
        
        Button(groupBox, text="Guardar", width=10, command=GuardarRegistro).grid(row=1, column=3, padx=0, pady=0)
        Button(groupBox, text="Modificar", width=10, command=ModificarRegistro).grid(row=2, column=3, padx=0, pady=0)
        Button(groupBox, text="Eliminar", width=10, command=EliminarRegistro).grid(row=3, column=3, padx=5, pady=0)
        Button(groupBox, text="Configurar base de datos", width=20, command=FormularioConfiguracion).grid(row=6, column=0, padx=5, pady=0)
        Button(groupBox, text="Actualizar", width=10, command=ActualizarTreeView).grid(row=4, column=3, padx=5, pady=0)
        
        groupBox = LabelFrame(base, text="listado de Alumnos",  padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=0)
        
        tree = ttk.Treeview(groupBox, columns=("Id", "Nombre", "Apellido", "DNI", "Fecha de Nacimiento", "Telefono", "Direccion", "Edad"),show="headings",height=30)
        tree.column("# 1", anchor="center", width=80, stretch="NO")
        tree.heading("Id", text="Id")
        tree.column("# 2", anchor="center", width=150, stretch="NO")
        tree.heading("Nombre", text="Nombre")
        tree.column("# 3", anchor="center", width=150, stretch="NO")
        tree.heading("Apellido", text="Apellido")
        tree.column("# 4", anchor="center", width=150, stretch="NO")
        tree.heading("DNI", text="DNI")
        tree.column("# 5", anchor="center", width=150, stretch="NO")
        tree.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
        tree.column("# 6", anchor="center", width=150, stretch="NO")
        tree.heading("Telefono", text="Telefono")
        tree.column("# 7", anchor="center", width=150, stretch="NO")
        tree.heading("Direccion", text="Direccion")
        tree.column("# 8", anchor="center", width=80, stretch="NO")
        tree.heading("Edad", text="Edad")
        
        if Configuracion.VerificarConfiguracion() == True and verificarVacio() == False:
            for row in CAlumnos.MostrarAlumnos(CConexion.ConexionBaseDeDatos()):
                tree.insert('', 'end', values=row)
        
        tree.bind("<<TreeviewSelect>>", SeleccionarRegistro)
                
        tree.pack()
        
        base.mainloop()
        
    except ValueError as error:
        print(f"Error al mostrar la interfaz, error {error}")


def GuardarRegistro():
    global textBoxNombre
    global textBoxApellido
    global textBoxDNI
    global PickerFechaNacimiento
    global textBoxTelefono
    global textBoxDireccion
    
    if Configuracion.VerificarConfiguracion() == False or verificarVacio() == True:
            messagebox.showerror("Error", "La configuracion de la base de datos no es correcta")
    else:
        conexion = CConexion.ConexionBaseDeDatos()
        try:
            if textBoxNombre is None or textBoxApellido is None or textBoxDNI is None or PickerFechaNacimiento is None or textBoxTelefono is None or textBoxDireccion is None:
                return
            
            nombres = textBoxNombre.get()
            if Verificacion.VerificarStringValido(nombres) == False:
                messagebox.showerror("Error", "El nombre no es valido, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            apellidos = textBoxApellido.get()
            if Verificacion.VerificarStringValido(apellidos) == False:
                messagebox.showerror("Error", "El apellido no es valido, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            dnis = textBoxDNI.get()
            if Verificacion.VerificarDNI(dnis) == False:
                messagebox.showerror("Error", "El DNI no es valido")
                return
            
            fechaNacimientos = PickerFechaNacimiento.get_date()
            
            telefonos = textBoxTelefono.get()
            if Verificacion.VerificarTelefono(telefonos) == False:
                messagebox.showerror("Error", "El telefono no es valido")
                return
            
            direcciones = textBoxDireccion.get()
            if Verificacion.VerificarStringValido(direcciones) == False:
                messagebox.showerror("Error", "La direccion no es valida, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            edad = Verificacion.CalcularEdad(PickerFechaNacimiento.get_date())
            if Verificacion.VerificarEdad(edad) == False:
                messagebox.showerror("Error", "La fecha no puede ser mayor a la actual")
                return
            
            CAlumnos.IngresarAlumno(conexion, nombres, apellidos, dnis, fechaNacimientos, telefonos, direcciones, edad)
            messagebox.showinfo("Informacion", "Datos guardados")
            
            #Actualizacion de vista
            ActualizarTreeView()
            
            #limpieza de campos    
            textBoxNombre.delete(0, END)
            textBoxApellido.delete(0, END)
            textBoxDNI.delete(0, END)
            PickerFechaNacimiento.delete(0, END)
            textBoxTelefono.delete(0, END)    
            textBoxDireccion.delete(0, END)
        
        except ValueError as error:
            print(f"Error al guardar los registros, error {error}")
        
def ModificarRegistro():
    
    global textBoxNombre
    global textBoxApellido
    global textBoxDNI
    global PickerFechaNacimiento
    global textBoxTelefono
    global textBoxDireccion
    
    if Configuracion.VerificarConfiguracion() == False or verificarVacio() == True:
            messagebox.showerror("Error", "La configuracion de la base de datos no es correcta")
    else:
        conexion = CConexion.ConexionBaseDeDatos()
        try:
            if textBoxNombre is None or textBoxApellido is None or textBoxDNI is None or PickerFechaNacimiento is None or textBoxTelefono is None or textBoxDireccion is None:
                return
            
            seleccionado = tree.focus()
            if seleccionado:
                values = tree.item(seleccionado)['values']
            
            idUsuario = values[0]
            nombres = textBoxNombre.get()
            if Verificacion.VerificarStringValido(nombres) == False:
                messagebox.showerror("Error", "El nombre no es valido, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            apellidos = textBoxApellido.get()
            if Verificacion.VerificarStringValido(apellidos) == False:
                messagebox.showerror("Error", "El apellido no es valido, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            dnis = textBoxDNI.get()
            print(type(dnis), dnis)
            if Verificacion.VerificarDNI(dnis) == False:
                messagebox.showerror("Error", "El DNI no es valido")
                return
            
            fechaNacimientos = PickerFechaNacimiento.get_date()
            
            telefonos = textBoxTelefono.get()
            if Verificacion.VerificarTelefono(telefonos) == False:
                messagebox.showerror("Error", "El telefono no es valido")
                return
            
            direcciones = textBoxDireccion.get()
            if Verificacion.VerificarStringValido(direcciones) == False:
                messagebox.showerror("Error", "La direccion no es valida, los siguentes caracteres no estan permitidos '.', ':', ';', ',', '´', '{', '}', '\\', '/'")
                return
            
            
            edad = Verificacion.CalcularEdad(PickerFechaNacimiento.get_date())       
            if Verificacion.VerificarEdad(edad) == False:
                messagebox.showerror("Error", "La fecha no puede ser mayor a la actual")
                return
            
            CAlumnos.ActualizarAlumno(conexion,idUsuario, nombres, apellidos, dnis, fechaNacimientos, telefonos, direcciones, edad)
            messagebox.showinfo("Informacion", "Datos Actualizados")
            
            #Actualizacion de vista
            ActualizarTreeView()
            
            #limpieza de campos
            textBoxNombre.delete(0, END)
            textBoxApellido.delete(0, END)
            textBoxDNI.delete(0, END)
            PickerFechaNacimiento.delete(0, END)
            textBoxTelefono.delete(0, END)    
            textBoxDireccion.delete(0, END)
        
        except ValueError as error:
            print(f"Error al guardar los registros, error {error}")

def EliminarRegistro():
    if Configuracion.VerificarConfiguracion() == False or verificarVacio() == True:
            messagebox.showerror("Error", "La configuracion de la base de datos no es correcta")
    else:
        try:
            seleccionado = tree.focus()
            if seleccionado:
                values = tree.item(seleccionado)['values']
                idUsuario = values[0]
                CAlumnos.EliminarAlumno(CConexion.ConexionBaseDeDatos(), idUsuario)
                messagebox.showinfo("Informacion", "Alumno Eliminado")
                
                #Actualizacion de vista
                ActualizarTreeView()
        except ValueError as error:
            print(f"Error al eliminar el registro, error {error}")
    

def ActualizarTreeView():
    global tree
    
    if Configuracion.VerificarConfiguracion() == False or verificarVacio() == True:
            messagebox.showerror("Error", "La configuracion de la base de datos no es correcta")
    else:
        try:
            tree.delete(*tree.get_children())
            
            datos = CAlumnos.MostrarAlumnos(CConexion.ConexionBaseDeDatos())
            
            for row in datos:
                tree.insert('', 'end', values=row)
                
        except ValueError as error:    
            print(f"Error al actualizar la lista de alumnos, error {error}")
        
def SeleccionarRegistro(event):
    try:
        seleccionado = tree.focus()
        
        if seleccionado:
            values = tree.item(seleccionado)['values']
            
            textBoxNombre.delete(0, END)
            textBoxNombre.insert(0, values[1])
            
            textBoxApellido.delete(0, END)
            textBoxApellido.insert(0, values[2])
            
            textBoxDNI.delete(0, END)
            textBoxDNI.insert(0, values[3])
            
            PickerFechaNacimiento.delete(0, END)
            PickerFechaNacimiento.insert(0, values[4])
            
            textBoxTelefono.delete(0, END)
            textBoxTelefono.insert(0, values[5])
            
            textBoxDireccion.delete(0, END)
            textBoxDireccion.insert(0, values[6])
            
    except ValueError as error:
        print(f"Error al seleccionar el registro, error {error}")
            

if Configuracion.VerificarConfiguracion() == False:
    FormularioConfiguracion()
Formulario()
    
    
