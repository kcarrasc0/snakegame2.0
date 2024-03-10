import tkinter as tk
from tkinter import messagebox
import random

class JogoPerguntaUnica:
    def __init__(self, perguntas_respostas):
        self.perguntas_respostas = perguntas_respostas
        self.fim_jogo = False
        self.root = tk.Tk()
        self.root.title("Pergunta Aleatória")
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        self.label_pergunta = tk.Label(self.root, text="")
        self.label_pergunta.pack()

        self.entry_resposta = tk.Entry(self.root)
        self.entry_resposta.pack()

        self.botao_enviar = tk.Button(self.root, text="Enviar", command=self.verificar_resposta)
        self.botao_enviar.pack()

        self.fim_jogo = False
        self.nova_pergunta_aleatoria()

    def centralizar_janela(self):
        largura = self.root.winfo_reqwidth()
        altura = self.root.winfo_reqheight()
        x = (self.root.winfo_screenwidth() - largura) // 2
        y = (self.root.winfo_screenheight() - altura) // 2
        self.root.geometry(f"+{x}+{y}")

    def nova_pergunta_aleatoria(self):
        self.centralizar_janela()  # Centralize a janela antes de exibir a pergunta
        pergunta_aleatoria = random.choice(self.perguntas_respostas)
        self.label_pergunta["text"] = pergunta_aleatoria[0]
        self.resposta_correta = pergunta_aleatoria[1].lower()
        self.entry_resposta.delete(0, tk.END)

    def verificar_resposta(self):
        resposta_usuario = self.entry_resposta.get().lower()

        if resposta_usuario == self.resposta_correta:
            messagebox.showinfo("Resposta Correta", "Você acertou!")
        else:
            messagebox.showerror("Resposta Incorreta", "Você errou!")
            self.fim_jogo = True

        self.root.destroy()

    def fechar_janela(self):
        messagebox.showerror("Resposta Incorreta", "Você errou!")
        self.fim_jogo = True
        self.root.destroy()

    def iniciar(self):
        self.root.mainloop()

# Matriz de perguntas e respostas
perguntas_respostas = [
    ["Qual é a capital do Brasil?", "Brasília"],
    ["Qual é a cor do céu em um dia ensolarado?", "Azul"],
    ["Quanto é 2 + 2?", "4"]
]

# Exemplo de uso:
if __name__ == "__main__":
    jogo = JogoPerguntaUnica(perguntas_respostas)
    jogo.iniciar()
