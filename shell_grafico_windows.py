import tkinter as tk
import os

def abrir_navegador():
    os.system("start chrome")

def abrir_editor():
    os.system("notepad")

def abrir_terminal():
    os.system("start powershell")

ventana = tk.Tk()
ventana.title("Shell Gráfico - Windows")
ventana.geometry("300x200")

tk.Button(ventana, text="1 Navegador", command=abrir_navegador).pack(pady=10)
tk.Button(ventana, text="2 Editor de Texto", command=abrir_editor).pack(pady=10)
tk.Button(ventana, text="3 Terminal", command=abrir_terminal).pack(pady=10)

ventana.mainloop()
