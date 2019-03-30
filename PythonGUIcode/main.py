from tkinter import *
import winsound
import threading
from display import Window
import sys
import os
import serial
import re
import string


sys.stdout.write("\n\nHello from Python %s\n\n\n" % (sys.version,))
os.system('DIR')
print(sys.hash_info)




def sound():
    print("Hallo there! do you wanna cheat on the quiz")
    winsound.PlaySound("Sound", winsound.SND_FILENAME)


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


def sirData():
    ser = serial.Serial()
    ser.port = 'COM4'
    ser.baudrate = 115200
    try:
        ser.open()
        print("The serial port is open? = ", ser.is_open)
    except:
        print("The serial port is open? = ", ser.is_open)


    while True:
        while ser.is_open:
            try:
                x = str(ser.readline())
                if "temp" in x:
                    temp = Search_number_String(x)
                    print("The temp from CC1310 is: ", temp)
                    global GSirDataTemp
                    GSirDataTemp = temp
                    print("wow ", GSirDataTemp)
            except:
                print("The serial port is not open anymore")
                ser.close()
                break
        try:
            ser.open()
        except:
            pass

    ser.close()


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600")
    app = Window(root)
    t1 = threading.Thread(target=sound)
    t1.start()
    root.mainloop()
    t1.join()




