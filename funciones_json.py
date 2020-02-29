import json

def listar_personajes(personajes):

    lista_nombres=[]
    lista_clase=[]
    for charac in personajes:
        
        lista_nombres.append(charac["name"])
        lista_clase.append(charac["_class"])
    return zip(lista_nombres, lista_clase)