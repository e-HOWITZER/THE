import tkinter as tk
import tkinter.ttk as ttk
import numpy
import cv2
class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.moveleft = tk.Button(self,width=20,height=2)
        self.moveleft["text"] = "Izquierda"
        self.moveleft["command"] = self.left
        self.moveleft.grid(row=1,column=0)
        self.moveright = tk.Button(self,width=20,height=2)
        self.moveright["text"] = "Derecha"
        self.moveright["command"] = self.right
        self.moveright.grid(row=1,column=1)
        self.shoot = tk.Button(self,width=40,height=2,fg="blue")
        self.shoot["text"] = "Disparo"
        self.shoot["command"] = self.launch
        self.shoot.grid(row=2,columnspan=2)
        self.end = tk.Button(self,width=20,height=2,text="Cerrar",command=self.quit,fg="red")
        self.end.grid(row=5,columnspan=2)
    def left(self):
        print("por ahora nada")
    def right(self):
        print("por ahora nada")
    def up(self):
        print("por ahora nada")
    def down(self):
        print("por ahora nada")
    def launch(self):
        print("por ahora nada")

root = tk.Tk()
root.title("THE")
root.geometry('300x500+100+300')
app = App(master=root)
app.mainloop()
