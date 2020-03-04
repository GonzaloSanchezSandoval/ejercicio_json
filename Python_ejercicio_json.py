import json
from funciones_json import *

with open ("Proyecto_2ºEvaluacion_Characters.json") as fichero:
    personajes = json.load(fichero)


while True:

    print("1- Lista el nombre y clase de todos los personajes.")
    print("2- Muestra los personajes que sean de la clase especifica introducida por teclado.")
    print("3- Muestra el aspecto de los personajes que tengan el pelo del color especifico introducido por teclado.")
    print("4- Di por teclado una habilidad y armadura con la que se tenga competencia y se mostrará por pantalla los personajes que tienen esa habilidad y pueden usar esa armadura.")
    print("5- Muestra el nombre, la clase y el sexo de los personajes que sean de un nivel especifico introducido por teclado y lleven un arma especifica introducida por teclado.")
    print("6- Salir del programa")

    eleccion=int(input("Selecciona la opción que quieras:"))

    if eleccion==1:
        
        for i in listar_personajes(personajes):
            print("Nombre:",i[0])
            print("Clase:",i[1])
        
    elif eleccion==2:
        clase=str(input("Introduce la clase que buscas:"))

        print(filtrar_por_clase(personajes, clase))
        

    elif eleccion==3:
        pelo=str(input("Introduce el color del pelo:"))

        print(filtrar_por_cabello(personajes, pelo))
     

    elif eleccion==4:
        armadura=str(input("Introduce una armadura:"))
        habilidad=str(input("Introduce una habilidad:"))
        print(filtrar_por_armadura_habilidad(personajes, armadura, habilidad))
        
    elif eleccion==5:
        arma=str(input("Introduce un arma:"))
        nivel=int(input("Introduce un nivel:"))
        print(filtrar_por_arma_nivel(personajes, arma, nivel))

    elif eleccion==6:
        print("Finalizando programa")
        break



    
    
    






