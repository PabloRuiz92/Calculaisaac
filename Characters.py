#Class Character
from os import stat
from Items import *

class Character():
    def __init__(self, nombre, vida , damage, tears, shotSpd, range, speed, luck):
        self.nombre = nombre
        self.vida= vida
        self.damage = round(damage,2)
        self.tears = tears
        self.shotSpd = shotSpd
        self.range = range
        self.speed = speed
        self.luck = luck

    def stat_up(self, item):
        self.vida += item["vida"]


charaIsaac=Character("Isaac" , 3 , (3.5*1.00) , 0 , 1 , 6.5 , 1.0 , 0 )

charaMadgalene=Character("Madgalene" , 4 , (3.5*1.00) , 0 , 1 , 6.5 , 0.85 ,0)

charaCain=Character("Cain" , 2 , (3.5*1.20), 0 , 1 , 4.5 , 1.3 , 0 )

charaJudas=Character("Judas", 1 , (3.5*1.35) , 0 , 1 ,6.5 , 1.0 , 0 )

charaDarkJudas=Character("Dark Judas" , 2 , (3.5*2.00) , 0 , 1 , 6.5 , 1.1 , 0 )

charaBlueBaby=Character("???" , 2 , (3.5*1.05) , 0 , 1 , 6.5 , 1.1 , 0 )

charaEve=Character("Eve" , 2 , (3.5*0.75) , 0 , 1 , 6.5 , 1.23 , 0 )

charaSamson=Character("Samson" , 3 , (3.5*1.0) , -0.1 , 1.31 , 5.0 , 1.1 , 0 )

#charaIsaac.stat_up(dinner)

#print(dinner)