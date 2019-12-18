from tkinter import *
from bazooka import *


class Rocket(object):
    
    def __init__(self,master,x,y,coul):
        self.master=master
        self.x=x
        self.y=y
        self.r=self.master.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill=coul)
    def destroy(self):
        self.master.delete(self.r)
        print("destruction")

    def envoie(self):
            global dx, dy
            self.master.move(balle1,dx,dy)
            #On repete cette fonction
            tk.after(20,deplacement)




