from tkinter import *
from PIL import ImageTk
from PIL import Image
import time
import serial
import re
import string

GSirDataTemp = 0

Message1 = "Flower Watering system"
Message2 = "The Humidity = "
Message2_5 = "The Sensor ID = "
Message3 = "Units"
Message4 = "100 %"
labeltext1 = str(0)
labeltext2 = str(0)
ownBg = '#FFFFFF'


def Search_number_String(String):
    index_list = []
    del index_list[:]
    for i, x in enumerate(String):
        if x.isdigit() == True:
            index_list.append(i)
    start = index_list[0]
    end = index_list[-1] + 1
    number = String[start:end]
    return number



class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.ser = serial.Serial()
        self.ser.port = 'COM4'
        self.ser.baudrate = 115200
        try:
            self.ser.open()
            print("The serial port is open? = ", self.ser.is_open)
        except:
            print("The serial port is open? = ", self.ser.is_open)
        self.temp = "N/A"
        self.ID = "NONE"
        self.count = 0
        self.update_label()




    def init_window(self):
        global ownBg
        orgBg = self.cget("background")
        ownBg = 'white'
        self.configure(bg = 'white')
        self.master.title("Watering Project (TNE090), By OSKAR KARLSSON")
        self.pack(fill=BOTH, expand=1)

        self.image1 = PhotoImage(file="plant.gif")
        self.photo1 = Label(self, image=self.image1,)
        self.photo1.place(x=300, y=380/2)

        self.image2 = PhotoImage(file="wateringA.gif")
        self.image2 = self.image2.subsample(2)

        self.photo2 = Label(self, image=self.image2, bg='white')
        self.photo2.place(x=545, y=101)

        self.label1 = Label(self, text= "INPUT COM PORT (default is COM4)", bg='white')
        self.label1.place(x=50, y=375)

        self.input1 = Entry(self, text="COM")
        self.input1.place(x=50, y=400)

        self.COM = Button(self, text="Execute", command=self.Execute)
        self.COM.place(x=50, y=425)

        self.label1 = Label(self, text= Message1 ,font=("Helvetica",32), bg='white')
        self.label1.place(x=150, y=50)

        self.label2 = Label(self, text=Message2, font=("Helvetica", 16), bg='white')
        self.label2.place(x=250, y=110)

        self.label3 = Label(self, text=labeltext1, font=("Helvetica", 16), bg='white')
        self.label3.place(x=450, y=110)

        self.labelID1 = Label(self, text=Message2_5, font=("Helvetica", 16), bg='white')
        self.labelID1.place(x=250, y=135)

        self.labelID2 = Label(self, text=labeltext2, font=("Helvetica", 16), bg='white')
        self.labelID2.place(x=450, y=135)


        self.label4 = Label(self, text=Message3, font=("Helvetica", 16), bg='white')
        self.label4.place(x=500, y=110)

        ###1
        self.box1 = Label(self ,width="3",height="1",bg="blue")
        self.box1.place(x=550, y=200)
        ###2
        self.box2 = Label(self, width="3", height="1", bg="blue")
        self.box2.place(x=550, y=220)
        ###3
        self.box3 = Label(self, width="3", height="1", bg="blue")
        self.box3.place(x=550, y=240)
        ###4
        self.box4 = Label(self, width="3", height="1", bg="blue")
        self.box4.place(x=550, y=260)
        ###5
        self.box5 = Label(self ,width="3",height="1",bg="blue")
        self.box5.place(x=550, y=280)
        ###6
        self.box6 = Label(self, width="3", height="1", bg="blue")
        self.box6.place(x=550, y=300)
        ###7
        self.box7 = Label(self, width="3", height="1", bg="blue")
        self.box7.place(x=550, y=320)
        ###8
        self.box8 = Label(self, width="3", height="1", bg="blue")
        self.box8.place(x=550, y=340)
        ###9
        self.box9 = Label(self, width="3", height="1", bg="blue")
        self.box9.place(x=550, y=360)
        ###10
        self.box10 = Label(self, width="3", height="1", bg="blue")
        self.box10.place(x=550, y=380)




        self.procent = Label(self, text=Message4, font=("Helvetica", 16), bg='white')
        self.procent.place(x=590, y=300)

    def Execute(self):
        INPUT1 = str(self.input1.get())
        self.ser.port = INPUT1


    def update_label(self):
        global ownBg
        self.label3.configure(text=str(self.temp))
        self.labelID2.configure(text=str(self.ID))
        self.label3.after(10, self.update_label)




        if self.ser.is_open:
            try:
                x = str(self.ser.readline())
                print(x)
            except:
                pass

            if "Sensor" in x:
                self.ID = Search_number_String(x)

            if "temp" in x:
                self.temp = Search_number_String(x)

            if self.temp != "N/A":
                y = int(self.temp)
                if y > 3000:
                    self.procent.configure(text="100 %")
                    self.box1.configure(bg="blue")
                    self.box2.configure(bg="blue")
                    self.box3.configure(bg="blue")
                    self.box4.configure(bg="blue")
                    self.box5.configure(bg="blue")
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 3000) & (y > 2700)):
                    self.procent.configure(text="90 %")
                    self.box1.configure(bg=ownBg )
                    self.box2.configure(bg="blue")
                    self.box3.configure(bg="blue")
                    self.box4.configure(bg="blue")
                    self.box5.configure(bg="blue")
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 2700) & (y > 2400)):
                    self.procent.configure(text="80 %")
                    self.box1.configure(bg=ownBg )
                    self.box2.configure(bg=ownBg )
                    self.box3.configure(bg="blue")
                    self.box4.configure(bg="blue")
                    self.box5.configure(bg="blue")
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y  < 2400) & (y > 2100)):
                    self.procent.configure(text="70 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg="blue")
                    self.box5.configure(bg="blue")
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 2100) & (y > 1800)):
                    self.procent.configure(text="60 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg="blue")
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 1800) & (y > 1500)):
                    self.procent.configure(text="50 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg="blue")
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 1500) & (y > 1200)):
                    self.procent.configure(text="40 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg=ownBg)
                    self.box7.configure(bg="blue")
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 1200) & (y > 900)):
                    self.procent.configure(text="30 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg=ownBg)
                    self.box7.configure(bg=ownBg)
                    self.box8.configure(bg="blue")
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 900) & (y > 600)):
                    self.procent.configure(text="20 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg=ownBg)
                    self.box7.configure(bg=ownBg)
                    self.box8.configure(bg=ownBg)
                    self.box9.configure(bg="blue")
                    self.box10.configure(bg="blue")
                if ((y < 600) & (y > 300)):
                    self.procent.configure(text="10 %")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg=ownBg)
                    self.box7.configure(bg=ownBg)
                    self.box8.configure(bg=ownBg)
                    self.box9.configure(bg=ownBg)
                    self.box10.configure(bg="blue")
                if (y < 300):
                    self.procent.configure(text="Torr!")
                    self.box1.configure(bg=ownBg)
                    self.box2.configure(bg=ownBg)
                    self.box3.configure(bg=ownBg)
                    self.box4.configure(bg=ownBg)
                    self.box5.configure(bg=ownBg)
                    self.box6.configure(bg=ownBg)
                    self.box7.configure(bg=ownBg)
                    self.box8.configure(bg=ownBg)
                    self.box9.configure(bg=ownBg)
                    self.box10.configure(bg=ownBg)


