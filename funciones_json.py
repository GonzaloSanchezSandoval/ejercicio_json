import json

def listar_personajes(personajes):

    lista_nombres=[]
    lista_clase=[]
    for charac in personajes:
        
        lista_nombres.append(charac["name"])
        lista_clase.append(charac["_class"])
    return zip(lista_nombres, lista_clase)

def filtrar_por_clase(personajes, clase):
    contador = 0
    for charac in personajes:
            
        lista_nombres=[]
        lista_clase=[]
        
        if charac["_class"] == clase:
            contador = contador + 1
    return contador


def filtrar_por_cabello(personajes, pelo):

    for charac in personajes:
        
        personaje=charac["aspect"][0]["hairColor"]

        if personaje.count(pelo)>=1:
            print("Nombre:",charac["name"])
            print("Color de ojos:",charac["aspect"][0]["eyeColor"])
            print("Color de piel:",charac["aspect"][0]["skincolor"])

def filtrar_por_armadura_habilidad(personajes, armadura, habilidad):

    for charac in personajes:

        if charac["proficiencies"][0]["items_proficiencies"][0]["armors"].count(armadura)>=1 and charac["proficiencies"][1]["personal_profinciencies"][1]["abilities"].count(habilidad)>=1:
            print("Nombre:",charac["name"])


def filtrar_por_arma_nivel(personajes, arma, nivel):

    for charac in personajes:

        if charac["weapons"][0]["weapon"].count(arma)>=1 and charac["level"]==nivel:
            print("Nombre:",charac["name"])
            print("Clase:",charac["_class"])
            print("Sexo:",charac["gender"])
            
        