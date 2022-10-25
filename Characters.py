#Class Character
from Items import *
from math import pow

class Character():
    def __init__(self, nombre, vida, mutiplicador, damage, tears, shotSpd, rango, speed, luck, imagen):
        self.nombre = nombre
        self.vida= vida
        self.mutiplicador = mutiplicador
        self.damage = f"{damage*self.mutiplicador:.2f}"
        self.tears = tears
        self.shotSpd = shotSpd
        self.rango = rango
        self.speed = speed
        self.luck = luck
        self.imagen = imagen


    def stat_up(self, item):
        self.vida += item["vida"]


Isaac=Character("Isaac" , 3 , 1.00 , 3.5 , 0 , 1 , 6.5 , 1.0 , 0 ,"charas\Isaac.png")

Madgalene=Character("Madgalene" , 4 , 1.00 , 3.5 , 0 , 1 , 6.5 , 0.85 , 0, "charas\Madgalena.png")

Cain=Character("Cain" , 2 , 1.20 , 3.5 , 0 , 1 , 4.5 , 1.3 , 0 ,"charas\Isaac.png")

Judas=Character("Judas", 1 , 1.35 , 3.5 , 0 , 1 ,6.5 , 1.0 , 0 ,"charas\Isaac.png")

DarkJudas=Character("Dark Judas" , 2 , 2.00 , 3.5 , 0 , 1 , 6.5 , 1.1 , 0 ,"charas\Isaac.png")

BlueBaby=Character("???" , 3 , 1.05 , 3.5 , 0 , 1 , 6.5 , 1.1 , 0 ,"charas\Isaac.png")

Eve=Character("Eve" , 2 , 0.75 , 3.5 , 0 , 1 , 6.5 , 1.23 , 0 ,"charas\Isaac.png")

Samson=Character("Samson" , 3 , 1.00 , 3.5 , -0.1 , 1.31 , 5.0 , 1.1 , 0 ,"charas\Isaac.png")

#Isaac.stat_up(dinner)
#print(Isaac.damage)