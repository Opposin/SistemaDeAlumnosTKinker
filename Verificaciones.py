import datetime



class Verificacion:   
    def CalcularEdad(fechaNacimiento):
        #Calcula la edad en base a la fecha actual y la fecha de nacimiento
        try:      
            if fechaNacimiento != None:             
                hoy = datetime.date.today()
                edad = hoy.year - fechaNacimiento.year - ((hoy.month, hoy.day) < (fechaNacimiento.month, fechaNacimiento.day))
                
                return edad
            else:
                return None
        
        except ValueError as error:
            print(f"Error al calcular la edad, error {error}")
            
    def VerificarEdad(edad):
        #Verifica que la edad sea 0 o mayor
        if edad < 0:
            return False
        else:
            return True
        
    def VerificarDNI(DNI):
    #Verificar que el DNI sea un numero entero no negativo de 8 digitos
        if isinstance(DNI, str) and DNI.isdigit() and len(DNI) <= 8:
            return True
        else:
            return False
    
    def VerificarTelefono(telefono):
    #Verificar que el DNI sea un numero entero no negativo de 8 digitos
        if isinstance(telefono, str) and telefono.isdigit() and len(telefono) in range(10, 15) or telefono == "":
            return True
        else:
            return False
        
    def VerificarStringValido(variable):
    # Caracteres prohibidos
        caracteres_prohibidos = ['.', ':', ';', ',', "'", '"', '|', '°', '´', '{', '}', '\\', '/']
        
        # Verifica si la variable es un string, tiene menos o igual a 25 caracteres y no contiene caracteres prohibidos
        if isinstance(variable, str) and variable != "" and len(variable) <= 25 and not any(caracter in variable for caracter in caracteres_prohibidos):
            return True
        else:
            return False