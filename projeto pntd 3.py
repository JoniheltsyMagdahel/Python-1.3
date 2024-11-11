#Importando a biblioteca  
import tkinter as tk
from tkinter import messagebox
#Criando  a janela
#dando o nome para  a janela
#espessura  e altura da janela
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x500")

#criando a barra de texto
#local onde a barra de texto ficara
entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.pack(pady=5)

#criando a lista
#espessura da lista
listbox = tk.Listbox(janela)
listbox.pack(pady=10)

# adiciona esse texto em uma lista (como uma Listbox), 
# e depois limpa o campo de entrada para que o usuário 
# possa adicionar uma nova tarefa, se desejar.
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        listbox.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

#exclusão  de tarefa
def excluir_tarefa():
    listbox.delete(tk.ANCHOR)

#Se houver seleção
#Deleta o item selecionado
def concluir():
    selecao = listbox.curselection()
    if selecao:  # Verifica se há um item selecionado
        index = selecao[0]  # Seleciona o índice do item
        item = listbox.get(index)  # Obtém o texto do item selecionado
        listbox.delete(index)  # Remove o item da listbox
        # Adiciona o item de volta com o texto modificado (por exemplo, "Concluído" no final)
        listbox.insert(index, item + "Concluído")
    else:
        print("Selecione uma tarefa para concluir")

    

#adicionando Tarefas 
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)
#excluindo  tarefas
botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa)
botao_excluir.pack(pady=5)
#concluindo  tarefas
botao_concluir =  tk.Button(janela, text="Concluir", command=concluir)
botao_concluir.pack(pady=5)


janela.mainloop()
