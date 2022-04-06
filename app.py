from tkinter import *
import time
from tkinter.ttk import Treeview
from treeview import tab

master = Tk()
master.title("Xperience")
master.geometry("490x560+610+153")
master.iconbitmap(default="LOGIN.png")
master.resizable(width=1, height=1)


#Funçoes

def nova_janela():

    time.sleep(0.5)
    master.destroy()
    
    tab()
    #master1 = Tk()
    #master1.title("Nova Janela criada!!")
    #master1.geometry("490x560+400+153")

# variaveis globais
esconde_senha = StringVar()

#importar imagens
img_fundo = PhotoImage(file="LOGIN.png")
img_botao = PhotoImage(file="LOGINbtn.png")
#criação de label

lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

#criação de caixas de entrada
en_user = Entry(master,bd=2, font=("Calibri", 15), justify=CENTER)
en_user.place(width=233, height=38, x=128, y=240)

en_password = Entry(master,textvariable=esconde_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_password.place(width=233, height=38, x=128, y=310)


# BOTTON

bt_login = Button(master, bd=0, image=img_botao, command=nova_janela)
bt_login.place(width=120, height=40, x=185, y=380)
master.mainloop()