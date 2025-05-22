import tkinter as tk
from tkinter import ttk, messagebox

class NotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Notas")
        self.listaNotas = []

        # Entrada de nota
        tk.Label(root, text="Digite a nota:").pack(pady=5)
        self.entry_nota = tk.Entry(root)
        self.entry_nota.pack(pady=5)

        # Botão para adicionar nota
        tk.Button(root, text="Adicionar Nota", command=self.adicionar_nota).pack(pady=5)

        # Botão para limpar a última nota
        tk.Button(root, text="Remover Última Nota", command=self.limpar_ultima_nota).pack(pady=5)

        # Botão para limpar toda a lista
        tk.Button(root, text="Limpar Lista", command=self.limpar_lista).pack(pady=5)

        # Tabela de notas
        self.tree = ttk.Treeview(root, columns=("Índice", "Nota"), show="headings")
        self.tree.heading("Índice", text="Índice")
        self.tree.heading("Nota", text="Nota")
        self.tree.pack(pady=5)

        # Botão para finalizar e mostrar estatísticas
        tk.Button(root, text="Finalizar e Mostrar Estatísticas", command=self.mostrar_estatisticas).pack(pady=5)

    def adicionar_nota(self):
        try:
            nota = float(self.entry_nota.get())
            if 0 <= nota <= 10:
                self.listaNotas.append(nota)
                self.tree.insert("", tk.END, values=(len(self.listaNotas), f"{nota:.1f}"))
                self.entry_nota.delete(0, tk.END)  # Limpa a caixa de texto
            else:
                messagebox.showerror("Erro", "Digite uma nota entre 0 e 10.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")

    def limpar_ultima_nota(self):
        if self.listaNotas:  # Verifica se há notas na lista
            self.listaNotas.pop()  # Remove a última nota
            self.tree.delete(self.tree.get_children()[-1])  # Remove a última linha da tabela
            messagebox.showinfo("Sucesso", "Última nota removida.")
        else:
            messagebox.showwarning("Aviso", "A lista de notas está vazia.")

    def limpar_lista(self):
        if self.listaNotas:  # Verifica se há notas na lista
            self.listaNotas.clear()  # Limpa toda a lista
            for item in self.tree.get_children():  # Remove todas as linhas da tabela
                self.tree.delete(item)
            messagebox.showinfo("Sucesso", "Lista de notas limpa.")
        else:
            messagebox.showwarning("Aviso", "A lista de notas já está vazia.")

    def mostrar_estatisticas(self):
        if self.listaNotas:
            total = sum(self.listaNotas)
            media = total / len(self.listaNotas)
            messagebox.showinfo("Estatísticas",
                                f"Quantidade de notas: {len(self.listaNotas)}\n"
                                f"Soma: {total:.1f}\n"
                                f"Média: {media:.1f}\n"
                                f"Maior nota: {max(self.listaNotas):.1f}\n"
                                f"Menor nota: {min(self.listaNotas):.1f}")
        else:
            messagebox.showinfo("Estatísticas", "Nenhuma nota adicionada.")

root = tk.Tk()
app = NotasApp(root)
root.mainloop()