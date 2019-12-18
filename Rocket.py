from tkinter import *
from bazooka import *


class Rocket(object):
    def __init__(self,parent,x,y,coul):
        self.parent=parent
        self.x, self.y = x, y
        self.r=self.parent.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill=coul)





