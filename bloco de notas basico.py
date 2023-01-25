import tkinter as tk
from tkinter import filedialog
import os

def salvar():
    texto = texto_widget.get("1.0", tk.END)
    arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All Files", "*.*")])
    if arquivo:
        arquivo.write(texto)
        arquivo.close()

def abrir():
    arquivo = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All Files", "*.*")])
    if arquivo:
        conteudo = arquivo.read()
        texto_widget.delete("1.0", tk.END)
        texto_widget.insert("1.0", conteudo)
        arquivo.close()

def sair():
    janela.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title("Bloco de Notas")

# Criar um widget de texto
texto_widget = tk.Text(janela)
texto_widget.pack()

# Criar um menu
menu = tk.Menu(janela)
janela.config(menu=menu)

# Criar os itens de menu
arquivo_menu = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Salvar", command=salvar)
arquivo_menu.add_command(label="Abrir", command=abrir)
arquivo_menu.add_command(label="Sair", command=sair)

# Executar a janela
janela.mainloop()
