import tkinter as tk
import functions

def initiate_gui():
    janela = tk.Tk()
    janela.title("Automate Gmail")
    janela.geometry("400x300")

    button_connect = tk.Button(janela, text="Conectar ao Gmail", command=functions.login())
    button_connect.pack()

    janela.mainloop()

