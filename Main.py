import cv2
import keyboard
import tkinter.ttk as ttk
import time
from tkinter import *
from subprocess import call








x = 0
s_t = time.time()


def on_button(event):
    global x



    if x == 1:
        print(f"{event.name} pressed")

        cam = cv2.VideoCapture(0)




        ret, frame = cam.read()

        if ret:

            cv2.imwrite("captured_image.png", frame)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Failed to capture image.")

        cam.release()
        call("") #here you can choose what the programm will open when somebody uses your pc without permmison :=)


    else:
        print("ts program or sum is off idk")









def cock():

    global x

    if x == 0:
       x = 1
       Ac.config(text="Stop :=(")




    else:
       x = 0
       Ac.config(text="Start muhehehe")
    keyboard.on_press(on_button)



root = Tk()





root.geometry("350x300")


root.title("Gotcha/dont use my pc cam :)")
root.resizable(width=False, height=False)



Padding = ttk.Frame(root, padding=10)
Padding.grid(column=0, row=1)

Padding1 = ttk.Frame(root, padding=10)
Padding1.grid(column= 0, row=0)


meowl = ttk.Label(Padding1,text="Uptime:")
meowl.grid(column=1, row=0)
drop = Label(root, text=" ")
donnie = ttk.Label(Padding1,text="00:00:00")
donnie.grid(column=2, row=0)
Ac = ttk.Button(Padding1, text="Start Muheheheh", command=lambda:cock() )
Ac.grid(column=3, row=0)







def aizen():
    if o.get() == "Aizen":
        print("aizen")
        logo = root.iconbitmap("logo.ico")
    elif o.get() == "Smile":
        print("smile")
        logo = root.iconbitmap("logo1.ico")
    elif o.get() == "Blank":
        print("Blank")
        logo = root.iconbitmap("Blank.ico")

logos = ["Aizen", "Smile", "Blank"]


o = StringVar(value="choose a logo :)")

OptionMenu(root, o, *logos).grid(column=0, row=1)

Button(root, text="Choose a logo", command=lambda:aizen()).grid(column=0 , row=2)








s_t = time.time()


def update_uptime():





    e = int(time.time() - s_t)

    h = e // 3600
    m = (e % 3600) // 60
    s = e % 60
    donnie.config(text=f"{h:02d}:{m:02d}:{s:02d}")










    root.after(1000, update_uptime)




update_uptime()





mainloop()
