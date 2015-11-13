

import Tkinter as TK
from serial import *


class TempMonitor():
    def __init__(self):
        self.mainWindow = TK.Tk()

        self.mainWindow.geometry("500x300+400+100")
        self.mainWindow.title("Monitor de Temperatura")
        self.mainWindow["bg"] = "gray"



        self.labelTemperatura = TK.Label(self.mainWindow,text="Temperatura:",bg="gray",borderwidth = 2,font=("arial",50))
        self.labelTemperatura.place(x= 110,y = 30)


        self.labelTemperaturaValor = TK.Label(self.mainWindow,text=" ",bg="gray",font=("arial",100))
        self.labelTemperaturaValor.place(x= 170,y = 100)


        self.getTempValue()
        self.mainWindow.mainloop()



    def getTempValue(self):
        arduino = Serial("/dev/cu.usbmodem1411",9600)
        tempValor = arduino.readline()
        #value = self.getTempValue()
        self.labelTemperaturaValor.configure(text = tempValor)
        self.mainWindow.after(100, self.getTempValue)
        arduino.close()


    # def update_clock(self):
    #     value = self.getTempValue()
    #     self.labelTemperaturaValor.configure(text = value )
    #     self.mainWindow.after(1000, self.update_clock)
      

