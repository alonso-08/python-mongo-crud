import time
from pymongo import MongoClient
from futbolista import Futbolista
from conexion import db

def pedir_numero_menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
    Futbolista('Iker','Casillas',33,['Portero'],True),
    Futbolista('Carles','Puyol',36,['Central', 'Lateral'],True),
    Futbolista('Sergio','Ramos',28,['Lateral','Central'],True),
    Futbolista('Andrés','Iniesta',30,['Centrocampista','Delantero'],True),
    Futbolista('Fernando','Torres',30,['Delantero'],True),
    Futbolista('Leo','Baptistao',22,['Delantero'],False)
]


#Obtenemos una coleccion para trabajar con ella
collection = db.futbolistas

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista
#Transformamos los objetos a diccionarios con la funcion to_db_collection
def insert_data_to_db(documentos):
    for futbolista in documentos:
        collection.insert(futbolista.to_db_collection())

def get_all_futbolistas():
    query=collection.find()
    for jugador in query:
        print(f'Nombre: {jugador["nombre"]}\nApellidos: {jugador["apellidos"]}\nEdad: {jugador["edad"]}\nDemarcacion: {jugador["demarcacion"]}\nInternacional: {jugador["internacional"]}')

def get_player_by_name(name):
    query=collection.find({"nombre":name})
    for jugador in query:
        print(f'Nombre: {jugador["nombre"]}\nApellidos: {jugador["apellidos"]}\nEdad: {jugador["edad"]}\nDemarcacion: {jugador["demarcacion"]}\nInternacional: {jugador["internacional"]}')


if __name__=='__main__':
    
    salir = False
    opcion = 0
    
    while not salir:
        print("..::::::: Menú :::::::...")
        print ("1. Insertar datos")
        print ("2. Consultar datos")
        print ("3. Consultar por nombre")
        print ("4. Eliminar datos")
        
        print ("Elige una opcion")
    
        opcion =  pedir_numero_menu()
    
        if opcion == 1:
            print ("Insertando datos a mongoDB...")
            time.sleep(3)
            insert_data_to_db(futbolistas)
            time.sleep(3)
            print ("Se insertaron correctamente")
        elif opcion == 2:
            print ("Obteniendo jugadores de la base de datos")
            time.sleep(3)
            print(get_all_futbolistas())
        elif opcion == 3:
            print("Consultando por nombre")
            time.sleep(3)
            name = str(input("Introduce un nombre: "))
            print(get_player_by_name(name))
            time.sleep(3)
            print("Consulta existosa")
        elif opcion == 4:
            print("En construccion")
        elif opcion==5:
            salir = True
        else:
            print ("¡No existe esa opción en el menú!")
    
    print ("Fin")
    