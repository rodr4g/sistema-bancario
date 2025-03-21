# Importação das bibliotecas necessárias
import tkinter as tk  # Para criar a interface gráfica
from tkinter import messagebox  # Para exibir caixas de diálogo (mensagens de sucesso ou erro)
import locale  # Para formatar valores monetários

# Configuração do locale para formatar valores monetários no padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Variáveis globais do sistema
saldo = 0  # Armazena o saldo atual da conta
limite = 500  # Define o valor máximo que pode ser sacado em uma única operação
extrato = ""  # Armazena o histórico de transações
numero_saques = 0  # Conta quantos saques foram realizados
LIMITE_SAQUES = 3  # Define o número máximo de saques permitidos

# Função para mostrar os campos de valor e o botão de confirmação
def mostrar_campos_valor():
    rotulo_valor.pack(pady=5)  # Exibe o rótulo "Valor:"
    entrada_valor.pack(pady=5)  # Exibe o campo de entrada para o valor
    botao_confirmar.pack(pady=5)  # Exibe o botão "Confirmar"

# Função para esconder os campos de valor e o botão de confirmação
def esconder_campos_valor():
    rotulo_valor.pack_forget()  # Esconde o rótulo "Valor:"
    entrada_valor.pack_forget()  # Esconde o campo de entrada para o valor
    botao_confirmar.pack_forget()  # Esconde o botão "Confirmar"

# Função para validar a entrada do usuário (garantir que seja um número positivo e fracionado)
def validar_entrada(texto):
    try:
        if texto == "" or texto == ".":
            return True  # Permite campo vazio ou ponto decimal
        valor = float(texto)  # Tenta converter o texto para float
        return valor >= 0  # Permite apenas números positivos
    except ValueError:
        return False  # Rejeita entradas inválidas (não numéricas)

# Função para formatar valores como moeda brasileira (R$ 50,75)
def formatar_moeda(valor):
    return locale.currency(valor, grouping=True, symbol=True)  # Formata o valor com símbolo R$ e separadores de milhar

# Função para iniciar o processo de depósito
def depositar():
    global saldo, extrato
    mostrar_campos_valor()  # Exibe os campos de valor
    botao_confirmar.config(command=confirmar_deposito)  # Configura o botão "Confirmar" para chamar a função de depósito

# Função para iniciar o processo de saque
def sacar():
    global saldo, extrato, numero_saques
    mostrar_campos_valor()  # Exibe os campos de valor
    botao_confirmar.config(command=confirmar_saque)  # Configura o botão "Confirmar" para chamar a função de saque

# Função para confirmar o depósito
def confirmar_deposito():
    global saldo, extrato
    valor = entrada_valor.get()  # Obtém o valor digitado pelo usuário
    try:
        valor = float(valor)  # Converte o valor para float
        if valor > 0:  # Verifica se o valor é positivo
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: {formatar_moeda(valor)}\n"  # Registra o depósito no extrato
            messagebox.showinfo("Sucesso", f"Depósito de {formatar_moeda(valor)} realizado com sucesso!")  # Exibe mensagem de sucesso
            entrada_valor.delete(0, tk.END)  # Limpa o campo de entrada
            esconder_campos_valor()  # Esconde os campos de valor após a operação
        else:
            messagebox.showerror("Erro", "O valor informado é inválido.")  # Exibe mensagem de erro se o valor for inválido
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido! Digite um número.")  # Exibe mensagem de erro se a conversão falhar

# Função para confirmar o saque
def confirmar_saque():
    global saldo, extrato, numero_saques
    valor = entrada_valor.get()  # Obtém o valor digitado pelo usuário
    try:
        valor = float(valor)  # Converte o valor para float
        excedeu_saldo = valor > saldo  # Verifica se o valor excede o saldo
        excedeu_limite = valor > limite  # Verifica se o valor excede o limite por operação
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques foi atingido

        if excedeu_saldo:
            messagebox.showerror("Erro", "Você não tem saldo suficiente.")  # Exibe mensagem de erro se o saldo for insuficiente
        elif excedeu_limite:
            messagebox.showerror("Erro", "O valor do saque excede o limite.")  # Exibe mensagem de erro se o limite for excedido
        elif excedeu_saques:
            messagebox.showerror("Erro", "Número máximo de saques excedido.")  # Exibe mensagem de erro se o número de saques for excedido
        elif valor > 0:  # Verifica se o valor é positivo
            saldo -= valor  # Atualiza o saldo
            extrato += f"Saque: {formatar_moeda(valor)}\n"  # Registra o saque no extrato
            numero_saques += 1  # Incrementa o número de saques realizados
            messagebox.showinfo("Sucesso", f"Saque de {formatar_moeda(valor)} realizado com sucesso!")  # Exibe mensagem de sucesso
            entrada_valor.delete(0, tk.END)  # Limpa o campo de entrada
            esconder_campos_valor()  # Esconde os campos de valor após a operação
        else:
            messagebox.showerror("Erro", "O valor informado é inválido.")  # Exibe mensagem de erro se o valor for inválido
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido! Digite um número.")  # Exibe mensagem de erro se a conversão falhar

# Função para exibir o extrato
def ver_extrato():
    global extrato, saldo
    extrato_formatado = "Não foram realizadas movimentações." if not extrato else extrato  # Verifica se há movimentações
    messagebox.showinfo("Extrato", f"================ EXTRATO ================\n{extrato_formatado}\nSaldo: {formatar_moeda(saldo)}\n=======================================")  # Exibe o extrato formatado

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal
janela.title("Sistema Bancário")  # Define o título da janela
janela.geometry("300x300")  # Define o tamanho da janela (300x200 pixels)

# Função de validação para o campo de entrada
validacao = janela.register(validar_entrada)  # Registra a função de validação

# Rótulo e entrada para o valor (inicialmente escondidos)
rotulo_valor = tk.Label(janela, text="Valor:")  # Cria o rótulo "Valor:"
entrada_valor = tk.Entry(janela, validate="key", validatecommand=(validacao, "%P"))  # Cria o campo de entrada com validação
botao_confirmar = tk.Button(janela, text="Confirmar")  # Cria o botão "Confirmar"

# Botões para as operações
botao_depositar = tk.Button(janela, text="Depositar", command=depositar)  # Botão para depósito
botao_depositar.pack(pady=5)  # Exibe o botão na janela

botao_sacar = tk.Button(janela, text="Sacar", command=sacar)  # Botão para saque
botao_sacar.pack(pady=5)  # Exibe o botão na janela

botao_extrato = tk.Button(janela, text="Extrato", command=ver_extrato)  # Botão para extrato
botao_extrato.pack(pady=5)  # Exibe o botão na janela

botao_sair = tk.Button(janela, text="Sair", command=janela.quit)  # Botão para sair do programa
botao_sair.pack(pady=5)  # Exibe o botão na janela

# Iniciar a interface
janela.mainloop()  # Inicia o loop principal da interface gráfica
