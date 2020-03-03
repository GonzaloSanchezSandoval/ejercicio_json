import json

def listar_personajes(personajes):

    lista_nombres=[]
    lista_clase=[]
    for charac in personajes:
        
        lista_nombres.append(charac["name"])
        lista_clase.append(charac["_class"])
    return zip(lista_nombres, lista_clase)

def filtrar_por_clase(personajes, clase):

    for charac in personajes:
        
        personaje=charac["_class"]
        lista_nombres=[]
        lista_clase=[]
        if personaje.count(clase)>=1:
            lista_nombres.append(charac["name"])
            lista_clase.append(charac["_class"])
        return zip(lista_nombres, lista_clase)


def filtrar_por_cabello(personajes, pelo):

    for charac in personajes:
        
        personaje=charac["aspect"]["hairColor"]
        lista_nombres=[]
        lista_aspecto=[]
        if personaje.count(clase)>=1:
            lista_nombres.append(charac["name"])
            lista_aspecto.append(charac["aspect"])
        return zip(lista_nombres, lista_aspecto)