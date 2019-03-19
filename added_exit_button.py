import Tkinter


interface = Tkinter.Tk()

def But1():
   interface.quit()





button1 = Tkinter.Button(interface, text="Button1",command = But1)

button1.grid(row=1, column=0)


interface.mainloop()


