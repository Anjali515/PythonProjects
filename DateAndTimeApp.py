#Python GUI App to print current Date & Time
from tkinter import *
from tkinter import ttk
import datetime
def LogCurTime():
    now = datetime.datetime.now()
    #print ("Current date and time : ")
    #print (now.strftime("%Y-%m-%d %H:%M:%S"))
    Createstatus.set(now.strftime("%Y-%m-%d %H:%M:%S"))
    return

root = Tk()
root.geometry("400x100+100+100")
root.title("Python Current Date And Time GUI App")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Current date and time :").grid(column=1, row=1, sticky=W)
Createstatus = StringVar()
ttk.Label(mainframe, textvariable=Createstatus).grid(column=2, row=1, sticky=(W, E))
b2 = ttk.Button(mainframe, text="ClickToPrint", command=LogCurTime).grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()