import Tkinter


interface = Tkinter.Tk()

def But1():
  print("Button1")


def But2():
  print("Button2")

def But3():
  print("Button3")


button1 = Tkinter.Button(interface, text="Button1",command = But1)

button1.grid(row=1, column=0)

button2 = Tkinter.Button(interface, text="Button2",command = But2)

button2.grid(row=2, column=0)

button3= Tkinter.Button(interface, text="Button3",command = But3)

button3.grid(row=3, column=0)

interface.mainloop()


