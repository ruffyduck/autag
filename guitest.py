from tkinter import *
import tkinter.filedialog

master = Tk()
master.wm_title("AuTag")
master.iconbitmap(default="resources/img.ico")


Label(master, text="caption").grid(row=0)
e = Entry(master, width=50)
e.grid(row=0, column=2)
e.insert(0, "Deine Mama")


e3 = Entry(master, width=2)
e3.grid(row=0, column=1)
e3.insert(0, "1")

Label(master, text="captioasdasdn").grid(row=1)
e2 = Entry(master, width=50)
e2.grid(row=1, column=2)
e2.insert(0, "Deine Mama")


#e.focus_set()

def callback():
    print (e.get())
    print (e2.get())
    e.delete(0, 'end')
    e.insert(0, "ayy")
    fileName = tkinter.filedialog.askdirectory()


opend = Button(master, text="open", width=10, command=callback)
opend.grid(row=2, column=0)



mainloop()



