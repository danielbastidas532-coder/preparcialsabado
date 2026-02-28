import random

def registrar_empleados():
    # Usamos input() para recibir datos y int() para convertir el texto a número
    try:
        numero_registros = int(input("Digite la cantidad de empleados a registrar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    lista_total_empleados = [] # Creamos la lista FUERA del ciclo para guardar a todos

    for intento in range(numero_registros):
        print(f"\n--- Registro del empleado {intento + 1} ---")
        
        # Generamos el ID
        id_empleado = random.randint(20000, 40000)
        
        # Capturamos los datos con input()
        nombre = input("Digite su nombre: ")
        doc = input("Digite su numero de documento: ")
        contrasena = input("Digite su contraseña: ")
        
        # Creamos el diccionario del empleado actual
        empleado = {
            "Id": id_empleado,
            "Nombre": nombre, 
            "Documento": doc,
            "Contrasena": contrasena
        }
        
        # Lo agregamos a nuestra lista global
        lista_total_empleados.append(empleado)
        
        print(f"✅ El/a empleado/a {nombre} con documento {doc} fue registrado con el ID: {id_empleado}")

    return lista_total_empleados

mis_empleados=registrar_empleados()

#Funcion login

def acceder_plataforma(documento_bd,contraseña_bd,numeroIntentos):
    for intento in range(1,numeroIntentos+1):
        documento_digitado=input("Documento: ")
        contraseña_digitada=input("Contraseña: ")
        if documento_digitado==documento_bd and contraseña_digitada==contraseña_bd:
            print("Bienvenido")
            return True
        else:
            print("Upss revisa")
    return False

#Funcion para general niveles de agua

import random

def generar_niveles_agua(cantidad):
    #Genera una lista de medidas de niveles de agua. Rango: 0 a 600
    
    lista_medidas = []
    
    for i in range(cantidad):
        # Generamos un número entero aleatorio
        medida = random.randint(0, 500)
        lista_medidas.append(medida)
        
    return lista_medidas

cantidad_a_generar = 200
niveles = generar_niveles_agua(cantidad_a_generar)

print(f"\nLista de medidas generadas: {niveles}")
print(f"Total de registros: {len(niveles)}")


#funcion para promediar el nivel del agua

def calcular_promedio_niveles(lista_medidas):
    #Calcula y devuelve el promedio de la lista recibida.
    if not lista_medidas:
        return 0
    
    suma_total = sum(lista_medidas)
    cantidad_elementos = len(lista_medidas)
    nivel_promedio_agua = suma_total / cantidad_elementos
    
    return nivel_promedio_agua

nivel_promedio= calcular_promedio_niveles(niveles)
print(f"El promedio de los niveles de agua generado fue de: {nivel_promedio}")


#Funcion para clasificar el agua

def clasificar_nivel_agua(nivel_promedio):
    if nivel_promedio>0 and nivel_promedio <=250:
        print(f"Nivel de agua muy bajo, favor apagar turbinas, el nivel fue de {nivel_promedio}")
    elif nivel_promedio>250 and nivel_promedio<=400:
        print(f"Nivel del agua optimo, el nivel fue de: {nivel_promedio}")
    elif nivel_promedio>400:
        print(f"Nivel de agua maximo, precaucion: elnivel de agua es de {nivel_promedio}")
    else:
        print("Nivel de agua no permitido")

promedio= clasificar_nivel_agua(nivel_promedio)





