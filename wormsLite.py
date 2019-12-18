from tkinter import *
from bazooka import *
from Rocket import *


# Code pour tester sommairement la classe Bazouka :
f = Tk()
can = Canvas(f,width =500, height =250, bg ='ivory')
#CANON 1
can.pack(padx =10, pady =10)
b1 = Bazooka(can, 50, 200)

#CANON 2
can.pack(padx =10, pady =10)
b2 = Bazooka(can, 450, 200)


#def deleteRocket(self):
    #can.delete(Rocket.r)
def CreateRocket():
    rocket1=Rocket(can,b1.x2,b1.y2,"red")
    f.after(20,CreateRocket)
    f.after(300,CreateRocket1)
    #f.after(30,deleteRocket)
def CreateRocket1():
    rocket2=Rocket(can,b2.x2,b2.y2,"red")
    f.after(20,CreateRocket1)
    f.after(300,CreateRocket1)
s1 =Scale(f, label='hausse', from_=90, to=0, command=b1.orienter)
s1.pack(side=LEFT, pady =15, padx =5)
s1.set(25)

s1 =Scale(f, label='hausse', from_=-270, to=-180, command=b2.orienter)
s1.pack(side=RIGHT, pady =15, padx =5)
s1.set(-205) # angle de tir initial




Bouton_Tir=Button(f, text ='Tir',command=CreateRocket)
Bouton_Tir.pack(side =LEFT, padx =3, pady =5)

Bouton_Shoot=Button(f, text ='Tir',command=CreateRocket1)
Bouton_Shoot.pack(side =RIGHT, padx =3, pady =5)

#Bouton_Destroy=Button(f, text ='Destroy',command=)
#Bouton_Destroy.pack()





f.mainloop()

