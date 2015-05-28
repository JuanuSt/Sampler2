__author__ = 'Juanu'

from tkinter import *
from tkinter import simpledialog
import os

# Directorio de trabajo
estamos = os.getcwd()
os.chdir(estamos)

class SAMPLE:
    # Atributos
    posicion= "" #Cualquier string que va delante del nombre del sonido, vale cualquier cosa.
    entrada = "" #El nombre del archivo
    fila=""      #Posicion en el grid
    column=""    #Posicion en el grid
    color=""     #Color de la frame

    # Metodos
    def __init__(self, pos, entrad, fil, col, colour): # el init es un constructor, una funcion especial que inicializa la clase.

        self.posicion = StringVar() #Para indicar el numero de la secuencia
        self.posicion.set(pos)

        self.defecto = StringVar() #Para reproducri la canción y poner el nombre del archivo
        self.defecto.set(entrad)

        self.suma = StringVar() #Para sumar el orden más el nombre del arcchivo
        self.suma.set (self.posicion.get() + self.defecto.get())


        def Lclic(event):
            self.test = self.defecto.get() # Por si pulsa play con el campo vacio
            if (self.test == "Empty" or self.test == None or self.test == "PY_VAR0"):
                TclError()
            else:
                cmd = "start " #'vlc --play-and-exit ' Para linux
                a = self.defecto.get()
                Play = cmd + a
                print(Play)
                #os.system (Play)

        def Rclic(event):
            entradanew = simpledialog.askstring("Sound File", "Enter new file")
            self.defecto.set(entradanew)
            p = self.posicion.get()
            self.suma.set(p + entradanew)
            print(entradanew)


        # Las cosas
        self.photo = PhotoImage(file="play.gif")
        self.sample = Frame(root, bg=colour, bd=5)
        self.boton = Button(self.sample,image=self.photo,width="50",height="25", anchor="c", bd=3)
        self.boton.pack(side=LEFT)
        self.boton.bind("<Button-1>",Lclic)
        self.boton.bind("<Button-3>",Rclic)
        self.hueco = Frame(self.sample, width=5, bg="black")
        self.hueco.pack(side=LEFT)
        self.label=Label(self.sample,textvariable=self.suma, fg="white", bg="black", width=25,bd=2, anchor="w")
        self.label.pack(side=RIGHT)
        self.sample.grid(row=fil, column=col)

root = Tk()
root.geometry("1140x480+150+150")
root.title("Sons 8 rutines")

fname=StringVar()
fname.set("backup.txt")


Boton01= SAMPLE("01.-", "Empty", 0, 0, "black")
Boton02= SAMPLE("02.-", "Empty", 1, 0, "black")
Boton03= SAMPLE("03.-", "Empty", 2, 0, "black")
Boton04= SAMPLE("04.-", "Empty", 3, 0, "green")
Boton05= SAMPLE("05.-", "Empty", 4, 0, "black")
Boton06= SAMPLE("06.-", "Empty", 5, 0, "black")
Boton07= SAMPLE("07.-", "Empty", 6, 0, "black")
Boton08= SAMPLE("08.-", "Empty", 7, 0, "black")
Boton09= SAMPLE("09.-", "Empty", 8, 0, "black")
Boton10= SAMPLE("10.-", "Empty", 9, 0, "black")

Boton11= SAMPLE("11.-", "Empty", 0, 1, "black")
Boton12= SAMPLE("12.-", "Empty", 1, 1, "black")
Boton13= SAMPLE("13.-", "Empty", 2, 1, "black")
Boton14= SAMPLE("14.-", "Empty", 3, 1, "black")
Boton15= SAMPLE("15.-", "Empty", 4, 1, "black")
Boton16= SAMPLE("16.-", "Empty", 5, 1, "black")
Boton17= SAMPLE("17.-", "Empty", 6, 1, "black")
Boton18= SAMPLE("18.-", "Empty", 7, 1, "black")
Boton19= SAMPLE("19.-", "Empty", 8, 1, "black")
Boton20= SAMPLE("20.-", "Empty", 9, 1, "black")

Boton21= SAMPLE("21.-", "Empty", 0, 2, "black")
Boton22= SAMPLE("22.-", "Empty", 1, 2, "black")
Boton23= SAMPLE("23.-", "Empty", 2, 2, "black")
Boton24= SAMPLE("24.-", "Empty", 3, 2, "black")
Boton25= SAMPLE("25.-", "Empty", 4, 2, "black")
Boton26= SAMPLE("26.-", "Empty", 5, 2, "black")
Boton27= SAMPLE("27.-", "Empty", 6, 2, "black")
Boton28= SAMPLE("28.-", "Empty", 7, 2, "black")
Boton29= SAMPLE("29.-", "Empty", 8, 2, "black")
Boton30= SAMPLE("30.-", "Empty", 9, 2, "black")

Boton31= SAMPLE("31.-", "Empty", 0, 3, "black")
Boton32= SAMPLE("32.-", "Empty", 1, 3, "black")
Boton33= SAMPLE("33.-", "Empty", 2, 3, "black")
Boton34= SAMPLE("34.-", "Empty", 3, 3, "black")
Boton35= SAMPLE("35.-", "Empty", 4, 3, "black")
Boton36= SAMPLE("36.-", "Empty", 5, 3, "black")
Boton37= SAMPLE("37.-", "Empty", 6, 3, "black")
Boton38= SAMPLE("38.-", "Empty", 7, 3, "black")
Boton39= SAMPLE("39.-", "Empty", 8, 3, "black")
Boton40= SAMPLE("40.-", "Empty", 9, 3, "black")


def SETRclic(event):
    nfname = simpledialog.askstring("Setting File", "Enter set file")
    fname.set(nfname)
    print(nfname)


def SETLclic(event):
    f= fname.get()
    fi=open(f, "r+")

    lista =[]
    for line in fi:
        line = line.rstrip('\n')
        lista.append(line)
    fi.close()

    l1=lista[0]
    l2=lista[1]
    l3=lista[2]
    l4=lista[3]
    l5=lista[4]
    l6=lista[5]
    l7=lista[6]
    l8=lista[7]
    l9=lista[8]
    l10=lista[9]
    l11=lista[10]
    l12=lista[11]
    l13=lista[12]
    l14=lista[13]
    l15=lista[14]
    l16=lista[15]
    l17=lista[16]
    l18=lista[17]
    l19=lista[18]
    l20=lista[19]
    l21=lista[20]
    l22=lista[21]
    l23=lista[22]
    l24=lista[23]
    l25=lista[24]
    l26=lista[25]
    l27=lista[26]
    l28=lista[27]
    l29=lista[28]
    l30=lista[29]
    l31=lista[30]
    l32=lista[31]
    l33=lista[32]
    l34=lista[33]
    l35=lista[34]
    l36=lista[35]
    l37=lista[36]
    l38=lista[37]
    l39=lista[38]
    l40=lista[39]

    Boton01= SAMPLE("01.-", l1, 0, 0, "black")
    Boton02= SAMPLE("02.-", l2, 1, 0, "black")
    Boton03= SAMPLE("03.-", l3, 2, 0, "black")
    Boton04= SAMPLE("04.-", l4, 3, 0, "black")
    Boton05= SAMPLE("05.-", l5, 4, 0, "black")
    Boton06= SAMPLE("06.-", l6, 5, 0, "black")
    Boton07= SAMPLE("07.-", l7, 6, 0, "black")
    Boton08= SAMPLE("08.-", l8, 7, 0, "black")
    Boton09= SAMPLE("09.-", l9, 8, 0, "black")
    Boton10= SAMPLE("10.-", l10, 9, 0, "black")

    Boton11= SAMPLE("11.-", l11, 0, 1, "black")
    Boton12= SAMPLE("12.-", l12, 1, 1, "black")
    Boton13= SAMPLE("13.-", l13, 2, 1, "black")
    Boton14= SAMPLE("14.-", l14, 3, 1, "black")
    Boton15= SAMPLE("15.-", l15, 4, 1, "black")
    Boton16= SAMPLE("16.-", l16, 5, 1, "black")
    Boton17= SAMPLE("17.-", l17, 6, 1, "black")
    Boton18= SAMPLE("18.-", l18, 7, 1, "black")
    Boton19= SAMPLE("19.-", l19, 8, 1, "black")
    Boton20= SAMPLE("20.-", l20, 9, 1, "black")

    Boton21= SAMPLE("21.-", l21, 0, 2, "black")
    Boton22= SAMPLE("22.-", l22, 1, 2, "black")
    Boton23= SAMPLE("23.-", l23, 2, 2, "black")
    Boton24= SAMPLE("24.-", l24, 3, 2, "black")
    Boton25= SAMPLE("25.-", l25, 4, 2, "black")
    Boton26= SAMPLE("26.-", l26, 5, 2, "black")
    Boton27= SAMPLE("27.-", l27, 6, 2, "black")
    Boton28= SAMPLE("28.-", l28, 7, 2, "black")
    Boton29= SAMPLE("29.-", l29, 8, 2, "black")
    Boton30= SAMPLE("30.-", l30, 9, 2, "black")

    Boton31= SAMPLE("31.-", l31, 0, 3, "black")
    Boton32= SAMPLE("32.-", l32, 1, 3, "black")
    Boton33= SAMPLE("33.-", l33, 2, 3, "black")
    Boton34= SAMPLE("34.-", l34, 3, 3, "black")
    Boton35= SAMPLE("35.-", l35, 4, 3, "black")
    Boton36= SAMPLE("36.-", l36, 5, 3, "black")
    Boton37= SAMPLE("37.-", l37, 6, 3, "black")
    Boton38= SAMPLE("38.-", l38, 7, 3, "black")
    Boton39= SAMPLE("39.-", l39, 8, 3, "black")
    Boton40= SAMPLE("40.-", l40, 9, 3, "black")

def SAVE():
    f=open("backup.txt", "w")
    f.write(Boton01.defecto.get()+ '\n')
    f.write(Boton02.defecto.get()+ '\n')
    f.write(Boton03.defecto.get()+ '\n')
    f.write(Boton04.defecto.get()+ '\n')
    f.write(Boton05.defecto.get()+ '\n')
    f.write(Boton06.defecto.get()+ '\n')
    f.write(Boton07.defecto.get()+ '\n')
    f.write(Boton08.defecto.get()+ '\n')
    f.write(Boton09.defecto.get()+ '\n')
    f.write(Boton10.defecto.get()+ '\n')

    f.write(Boton11.defecto.get()+ '\n')
    f.write(Boton12.defecto.get()+ '\n')
    f.write(Boton13.defecto.get()+ '\n')
    f.write(Boton14.defecto.get()+ '\n')
    f.write(Boton15.defecto.get()+ '\n')
    f.write(Boton16.defecto.get()+ '\n')
    f.write(Boton17.defecto.get()+ '\n')
    f.write(Boton18.defecto.get()+ '\n')
    f.write(Boton19.defecto.get()+ '\n')
    f.write(Boton20.defecto.get()+ '\n')

    f.write(Boton21.defecto.get()+ '\n')
    f.write(Boton22.defecto.get()+ '\n')
    f.write(Boton23.defecto.get()+ '\n')
    f.write(Boton24.defecto.get()+ '\n')
    f.write(Boton25.defecto.get()+ '\n')
    f.write(Boton26.defecto.get()+ '\n')
    f.write(Boton27.defecto.get()+ '\n')
    f.write(Boton28.defecto.get()+ '\n')
    f.write(Boton29.defecto.get()+ '\n')
    f.write(Boton30.defecto.get()+ '\n')

    f.write(Boton31.defecto.get()+ '\n')
    f.write(Boton32.defecto.get()+ '\n')
    f.write(Boton33.defecto.get()+ '\n')
    f.write(Boton34.defecto.get()+ '\n')
    f.write(Boton35.defecto.get()+ '\n')
    f.write(Boton36.defecto.get()+ '\n')
    f.write(Boton37.defecto.get()+ '\n')
    f.write(Boton38.defecto.get()+ '\n')
    f.write(Boton39.defecto.get()+ '\n')
    f.write(Boton40.defecto.get()+ '\n')

    f.close()



save = Button(root, text="Save", width=9,command=SAVE)
save.grid(row=10,column=0,pady=8)

sett = Button(root, text="Set", width=9,command=SAVE)
sett.grid(row=10,column=1,pady=8)
sett.bind("<Button-1>",SETLclic)
sett.bind("<Button-3>",SETRclic)

quitButton=Button(root, text='Quit',width=9,command=quit)
quitButton.grid(row=10,column=3,pady=8)


root.mainloop()
