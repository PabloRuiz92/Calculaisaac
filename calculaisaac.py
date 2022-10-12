from cProfile import label
from tkinter import *
from Characters import *
from Items import *

root=Tk()

#---Funciones--------------------
#Selector Personaje------------------
personaje=IntVar()
personajeSelection=StringVar()

def elegir_personage():

    if personaje.get()==1:
        personajeSelection.set(charaIsaac.nombre)
        vidaEntry.set(charaIsaac.vida)
        damageEntry.set(charaIsaac.damage)
        tearsEntry.set(charaIsaac.tears)
        shotSpdEntry.set(charaIsaac.shotSpd)
        rangeEntry.set(charaIsaac.range)
        speedEntry.set(charaIsaac.speed)
        luckEntry.set(charaIsaac.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Isaac.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

    elif personaje.get()==2:
        personajeSelection.set(charaMadgalene.nombre)
        vidaEntry.set(charaMadgalene.vida)
        damageEntry.set(charaMadgalene.damage)
        tearsEntry.set(charaMadgalene.tears)
        shotSpdEntry.set(charaMadgalene.shotSpd)
        rangeEntry.set(charaMadgalene.range)
        speedEntry.set(charaMadgalene.speed)
        luckEntry.set(charaMadgalene.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Madgalena.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

    elif personaje.get()==3:
        personajeSelection.set(charaCain.nombre)
        vidaEntry.set(charaCain.vida)
        damageEntry.set(charaCain.damage)
        tearsEntry.set(charaCain.tears)
        shotSpdEntry.set(charaCain.shotSpd)
        rangeEntry.set(charaCain.range)
        speedEntry.set(charaCain.speed)
        luckEntry.set(charaCain.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Madgalena.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

    elif personaje.get()==4:
        personajeSelection.set(charaJudas.nombre)
        vidaEntry.set(charaJudas.vida)
        damageEntry.set(charaJudas.damage)
        tearsEntry.set(charaJudas.tears)
        shotSpdEntry.set(charaJudas.shotSpd)
        rangeEntry.set(charaJudas.range)
        speedEntry.set(charaJudas.speed)
        luckEntry.set(charaJudas.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Madgalena.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

    elif personaje.get()==5:
        personajeSelection.set(charaDarkJudas.nombre)
        vidaEntry.set(charaDarkJudas.vida)
        damageEntry.set(charaDarkJudas.damage)
        tearsEntry.set(charaDarkJudas.tears)
        shotSpdEntry.set(charaDarkJudas.shotSpd)
        rangeEntry.set(charaDarkJudas.range)
        speedEntry.set(charaDarkJudas.speed)
        luckEntry.set(charaDarkJudas.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Madgalena.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

    elif personaje.get()==6:
        personajeSelection.set(charaBlueBaby.nombre)
        vidaEntry.set(charaBlueBaby.vida)
        damageEntry.set(charaBlueBaby.damage)
        tearsEntry.set(charaBlueBaby.tears)
        shotSpdEntry.set(charaBlueBaby.shotSpd)
        rangeEntry.set(charaBlueBaby.range)
        speedEntry.set(charaBlueBaby.speed)
        luckEntry.set(charaBlueBaby.luck)
        imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Madgalena.png")
        labelImage.config(image=imagenPersonaje)
        labelImage.image = imagenPersonaje

#Cambiar stats-----------------------
#cada check tiene que estar asociado a un item y cada item tiene que cambiar un stat correspondiente
#Los stats tendrian que estar asignados como [status, valor]

def statUp():
    item = dinnerCheck.cget("variable")
    #chara = "chara" + (cuadroNombre.get())
    if int(vidaEntry.get()) < 12:
        vidaEntry.set(item["vida"])



def healtup():
    item = dinnerCheck.cget("variable")
    for valor in item:
        if valor == "vida":
            vidaEntry.set(int(vidaEntry.get()) + int(item[valor]))

    if item == "dinner" and int(vidaEntry.get()) < 12:
        vidaEntry.set(int(vidaEntry.get()) + 1)

    #exec(""+ chara +".stat_up("+ item +")")



#------

root.title("CalculaIssac")

root.resizable(0,0)

root.geometry("380x350")

frame1=Frame(root)
frame1.grid()

#Colum_0
charaLabel=Label(frame1, text="Personaje:")
charaLabel.grid(row=1, column=0, sticky="W")

imagenPersonaje=PhotoImage(file="C:/cosas/Downloads/pildoras/phyton/calculaisaac/charas/Lost.png")
labelImage = Label(frame1, image=imagenPersonaje)
labelImage.grid(row=2, column=0, columnspan=2, rowspan=6, pady=5)

#Row_1 label/entry de personaje
cuadroNombre=Entry(frame1, textvariable=personajeSelection)
cuadroNombre.grid(row=1, column=1)


#Row_2  Label stats
vidaLabel=Label(frame1, text="Vida:")
vidaLabel.grid(row=1, column=2, sticky="W")

attackLabel=Label(frame1, text="Ataque:")
attackLabel.config()
attackLabel.grid(row=2, column=2, sticky="W")

tearsLabel=Label(frame1, text="Tears:")
tearsLabel.grid(row=3, column=2, sticky="W")

rangeLabel=Label(frame1, text="Shot Speed:")
rangeLabel.grid(row=4, column=2, sticky="W")

speedLabel=Label(frame1, text="Rango:")
speedLabel.grid(row=5, column=2, sticky="W")

tSpeedLabel=Label(frame1, text="Speed:")
tSpeedLabel.grid(row=6, column=2, sticky="W")

tHeigthLabel=Label(frame1, text="Luck:")
tHeigthLabel.grid(row=7, column=2, sticky="W")

#Row_3 Entry stats
vidaEntry=IntVar()
damageEntry=IntVar()
speedEntry=IntVar()
tearsEntry=IntVar()
shotSpdEntry=IntVar()
rangeEntry=IntVar()
speedEntry=IntVar()
luckEntry=IntVar()

cuadroVida=Entry(frame1, textvariable=vidaEntry, state="readonly", takefocus=False)
cuadroVida.grid(row=1, column=3)

cuadroDamage=Entry(frame1, textvariable=damageEntry, state="readonly", takefocus=False)
cuadroDamage.grid(row=2, column=3)

cuadroTears=Entry(frame1, textvariable=tearsEntry, state="readonly", takefocus=False)
cuadroTears.grid(row=3, column=3)

cuadroShotSpd=Entry(frame1, textvariable=shotSpdEntry, state="readonly", takefocus=False)
cuadroShotSpd.grid(row=4, column=3)

cuadroRange=Entry(frame1, textvariable=rangeEntry, state="readonly", takefocus=False)
cuadroRange.grid(row=5, column=3)

cuadroSpeed=Entry(frame1, textvariable=speedEntry, state="readonly", takefocus=False)
cuadroSpeed.grid(row=6, column=3)

cuadroLuck=Entry(frame1, textvariable=luckEntry, state="readonly", takefocus=False)
cuadroLuck.grid(row=7, column=3)

frame2=Frame(root)
frame2.grid()

#Botones de personaje--------------
#crear una funcione que genere los botones a partir de una base de datos de personajes?
IsaacRadio = Radiobutton(frame2, text="Isaac", variable=personaje, value=1, command=elegir_personage)
IsaacRadio.grid(row=0, column=0)
MadgaleneRadio = Radiobutton(frame2, text="Madgalene", variable=personaje, value=2, command=elegir_personage)
MadgaleneRadio.grid(row=0, column=1)
CainRadio = Radiobutton(frame2, text="Cain", variable=personaje, value=3, command=elegir_personage)
CainRadio.grid(row=0, column=2)
JudasRadio = Radiobutton(frame2, text="Judas", variable=personaje, value=4, command=elegir_personage)
JudasRadio.grid(row=0, column=3)
DJudasRadio = Radiobutton(frame2, text="Dark Judas", variable=personaje, value=5, command=elegir_personage)
DJudasRadio.grid(row=0, column=4)
BBabyRadio = Radiobutton(frame2, text="???", variable=personaje, value=6, command=elegir_personage)
BBabyRadio.grid(row=0, column=5)

#Selector Item-------------------------
frame3=Frame(root)
frame3.grid()
#crear una funcione que genere los botones a partir de una base de datos de items?
#dinner2 = "dinner"

dinnerCheck =Checkbutton(frame3, text="Dinner", variable = dinner["nombreItem"], command=healtup)
dinnerCheck.grid(row=0, column=1)

Checkbutton(frame3, text="<3").grid(row=0, column=2)
Checkbutton(frame3, text="20/20").grid(row=0, column=3)
Checkbutton(frame3, text="Aries").grid(row=0, column=4)

img_boton = PhotoImage(file=(dinner["ruta"]))
"""
boton = Button(frame3, text="dinner", textvariable=dinner, image=img_boton)
boton.grid(row=0, column=5)
"""
root.mainloop()