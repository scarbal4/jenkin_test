
import os
import pandas as pd
import matplotlib.pyplot as plt
import platform


class mascota():
    def __init__(self, animal, nombre_animal, sonido_emitido):
        print("Inicio Funcion __init__ en el modulo de principal.py")
        self.tipo_animal=animal
        self.nombre=nombre_animal
        self.sonido=sonido_emitido

    def Sonido_Animal(self):
        print("El {} que se llama {} lo que hace es {}" .format(self.tipo_animal, self.nombre, self.sonido))
        _privada()



def MiFuncion_Arranque():
    gato=mascota("gato", "misifu", "maulla")
    perro=mascota("perro", "Toby", "ladra")

    print(gato.Sonido_Animal())
    print(perro.Sonido_Animal())

def _privada():
    print("estoy dentro de la funcion privada")



if __name__ == "__main__":
    print ( "Ejecuto el Main y lo que hare sera llamar a la funcion de arranque")
    MiFuncion_Arranque()
