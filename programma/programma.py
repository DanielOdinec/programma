from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import fileinput
from tkinter.messagebox import*
root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")

def funktion(a):
    tabs.select(a)

def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=asksaveasfile(mode="W",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

def papich_image(name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)



tabs=ttk.Notebook(root)
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Seitsmes","Kaheksas"]
#or i in range(8):
  # tab=Frame(tabs)
   #tabs.add(tab,text=texts[i])

tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")


M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator="Command+V",command=lambda:funktion(0))
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_command(label="Tab3",command=lambda:funktion(2))
m1.add_command(label="Tab4",command=lambda:funktion(3))
m1.add_separator()

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Violet",command=lambda:root.config(bg="violet"))
m2.add_separator()

m3=Menu(M,tearoff=0)
M.add_cascade(label="Images",menu=m3)
m3.add_command(label="Papich1",command=lambda:papich_image("Papich1.png"))
m3.add_command(label="Papich2",command=lambda:papich_image("Papich2.png"))
m3.add_command(label="Papich3",command=lambda:papich_image("Papich3.png"))
m3.add_command(label="Papich4",command=lambda:papich_image("Papich4.png"))
m3.add_separator()

btn_open=Button(tab1,text="Open")
btn_save=Button(tab1,text="Save")
btn_exit=Button(tab1,text="Exit")
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
#Text(tab1,width=40,height
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

can=Canvas(tab2,width=300,height=200)
img=PhotoImage(file="Papich2.png").subsample(4)
can.create_image(10,10,image=img,anchor=NW)
can.pack()
tabs.pack(fill="both")
root.mainloop()

