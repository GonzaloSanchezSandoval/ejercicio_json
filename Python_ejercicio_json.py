import json
from funciones_json import *

with open ("Proyecto_2ºEvaluacion_Characters.json") as fichero:
    personajes = json.load(fichero)


for i in listar_personajes(personajes):
    print("Nombre:",i[0])
    print("Clase:",i[1])