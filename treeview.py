from tkinter import *
from tkinter import ttk


def tab():
    tabela = Tk()
    tabela.title("Curso")

    tree = ttk.Treeview(tabela, selectmode="browse", column=("column1", "column2", "column3"), show='headings')

    tree.column("column1", width=200,minwidth=50, stretch=NO)
    tree.heading("#1", text='Nome')

    tree.column("column2",width=100, minwidth=50, stretch=NO)
    tree.heading("#2", text='Idade')

    tree.column("column3", width=300, minwidth=50, stretch=NO)
    tree.heading("#3", text='Endereco')

    tree.grid(row=0,column=0)

    tabela.mainloop()




