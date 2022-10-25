from cProfile import label
from tkinter import *
from Characters import *
from Items import *

class Application(Frame):
    def __init__(self, master):
        self.personaje_selection=StringVar()
        self.frame_personaje_status=Frame(master)
        self.frame_personaje_status.grid()   

        self.chara_label=Label(self.frame_personaje_status, text="Personaje:")
        self.chara_label.grid(row=1, column=0, sticky="W")

        self.imagen_personaje= PhotoImage(file="charas\Lost.png")
        self.label_image =Label(self.frame_personaje_status, image=self.imagen_personaje)
        self.label_image.grid(row=2, column=0, columnspan=2, rowspan=6, pady=5)

        self.cuadro_nombre=Entry(self.frame_personaje_status, textvariable=self.personaje_selection)
        self.cuadro_nombre.grid(row=1, column=1)

        #Label y Entry stats-------------------
        self.vida=IntVar(value=0)
        self.damage=DoubleVar(value=0)
        self.tears=DoubleVar(value=0)
        self.shotSpd=IntVar(value=0)
        self.rango=DoubleVar(value=0)
        self.speed=DoubleVar(value=0)
        self.luck=DoubleVar(value=0)
        self.variables_stat = [self.vida,self.damage,self.tears,self.shotSpd,self.rango,self.speed,self.luck]
        self.status_lista =["vida","damage","tears","shotSpd","rango","speed","luck"]
        self.label_stat = []
        self.entry = []

        for stat in range(len(self.status_lista)):
            self.label_stat.append(Label(self.frame_personaje_status,
                                    text=self.status_lista[stat]))
            self.label_stat[stat].grid(row=stat+1, column=2, sticky="W")

            self.entry.append(Entry(self.frame_personaje_status, 
                                    textvariable=self.variables_stat[stat], 
                                    state="readonly", 
                                    takefocus=False))
            self.entry[stat].grid(row=stat+1, column=3)

        #Radiales de personaje--------------
        self.frame_radiales_personaje=Frame(root)
        self.frame_radiales_personaje.grid()

        self.personaje=IntVar(value=0)
        self.personajes_lista =[Isaac,Madgalene,Cain,Judas,DarkJudas,BlueBaby,Eve,Samson]
        self.radio_personaje=[]
        for caracter in range(len(self.personajes_lista)):
            self.radio_personaje.append(Radiobutton(
                self.frame_radiales_personaje, 
                text=(self.personajes_lista[caracter]).nombre,
                variable=self.personaje, 
                value=caracter+1, 
                command=lambda: self.elegir_personage(self.personajes_lista[(self.personaje.get())-1])))
            self.radio_personaje[caracter].grid(row=0, column=caracter+1, sticky="W")

        #Botones de Item--------------
        self.frame_botones_item=Frame(root)
        self.frame_botones_item.grid(column=0, row=7, columnspan=2)

        self.row_contador = 0
        column_contador = 5
        self.botones_item=[]
        self.img_boton=[]
        for item in items:
            self.img_boton.append(PhotoImage(file=(items[item]['ruta'])))
            self.botones_item.append(Button(self.frame_botones_item,
                                            image=self.img_boton[item], 
                                            command=lambda item = item: self.stat_up(item)))
            self.botones_item[item].grid(row=0, column=column_contador)
            column_contador += 1

    #Metodos-------------------
    def elegir_personage(self, personaje_elegido):
        self.personaje_selection.set(personaje_elegido.nombre)
        contador=0
        for i in self.variables_stat:
            i.set(personaje_elegido.__getattribute__(self.status_lista[contador]))
            contador+=1
        imagen_personaje=PhotoImage(file=personaje_elegido.imagen)
        self.label_image.config(image=imagen_personaje)
        self.label_image.image = imagen_personaje

    def stat_up(self, item):
        for valor in items[item]:
            if valor in self.status_lista:
                index = self.status_lista.index(valor)
                self.valor = self.variables_stat[index]
                cambio=(self.valor.get()+items[item][valor])
                self.valor.set(cambio)
                if self.vida.get() > 12:
                    self.vida.set(12)
                if self.tears.get() > 120:
                    self.tears.set(120)
                if self.speed.get() > 2.0:
                    self.speed.set(2.0)   

#Main-------------------
root=Tk()
root.title("CalculaIssac")
root.resizable(0,0)
root.geometry("380x350")

app = Application(root)

root.mainloop()