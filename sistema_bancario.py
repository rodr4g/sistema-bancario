# Importação das bibliotecas necessárias
import tkinter as tk  # Para criar a interface gráfica
from tkinter import messagebox  # Para exibir caixas de mensagem
import locale  # Para formatação monetária
from datetime import datetime  # Para registrar data e hora das transações

# Configura o locale para o formato brasileiro (R$)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Variáveis globais do sistema bancário
saldo = 0  # Armazena o saldo atual da conta
limite = 500  # Limite máximo por saque
extrato = ""  # Armazena o histórico de transações
numero_saques = 0  # Contador de saques realizados
numero_transacoes = 0  # Contador geral de transações
LIMITE_SAQUES = 3  # Número máximo de saques permitidos
LIMITE_TRANSACOES = 10  # Número máximo total de transações permitidas por dia

def mostrar_campos_valor():
    """Exibe os campos para inserção de valor e botão de confirmação"""
    rotulo_valor.pack(pady=5)  # Mostra o rótulo "Valor:"
    entrada_valor.pack(pady=5)  # Mostra o campo de entrada
    botao_confirmar.pack(pady=5)  # Mostra o botão Confirmar

def esconder_campos_valor():
    """Oculta os campos de valor e limpa a entrada"""
    rotulo_valor.pack_forget()  # Esconde o rótulo
    entrada_valor.pack_forget()  # Esconde o campo de entrada
    botao_confirmar.pack_forget()  # Esconde o botão
    entrada_valor.delete(0, tk.END)  # Limpa o conteúdo do campo

def validar_entrada(texto):
    """Valida se a entrada é um número positivo"""
    try:
        if texto in ("", "."):  # Permite campo vazio ou ponto decimal
            return True
        return float(texto) >= 0  # Só aceita números positivos
    except ValueError:
        return False  # Rejeita entradas não numéricas

def formatar_moeda(valor):
    """Formata valores no padrão monetário brasileiro"""
    return locale.currency(valor, grouping=True, symbol=True)

def registrar_transacao(tipo, valor):
    """Registra uma transação no extrato com data/hora"""
    global extrato, numero_transacoes
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém data/hora atual
    extrato += f"{tipo}: {formatar_moeda(valor)} (em {data_hora})\n"  # Adiciona ao extrato
    numero_transacoes += 1  # Incrementa contador

def verificar_limite_transacoes():
    """Verifica se atingiu o limite diário de transações"""
    if numero_transacoes >= LIMITE_TRANSACOES:
        messagebox.showerror("Erro", f"Limite de {LIMITE_TRANSACOES} transações diárias atingido!")
        return True
    return False

def depositar():
    """Prepara a interface para depósito"""
    if verificar_limite_transacoes():  # Verifica limite antes de continuar
        return
    mostrar_campos_valor()  # Mostra campos de valor
    botao_confirmar.config(command=confirmar_deposito)  # Configura botão

def sacar():
    """Prepara a interface para saque"""
    if verificar_limite_transacoes():  # Verifica limite antes de continuar
        return
    mostrar_campos_valor()  # Mostra campos de valor
    botao_confirmar.config(command=confirmar_saque)  # Configura botão

def confirmar_deposito():
    """Executa a operação de depósito"""
    global saldo
    valor = entrada_valor.get()  # Obtém valor digitado
    try:
        valor = float(valor)  # Converte para número
        if valor > 0:  # Valida valor positivo
            saldo += valor  # Atualiza saldo
            registrar_transacao("Depósito", valor)  # Registra transação
            messagebox.showinfo("Sucesso", f"Depósito de {formatar_moeda(valor)} realizado!")
            esconder_campos_valor()  # Limpa interface
        else:
            messagebox.showerror("Erro", "Valor deve ser positivo!")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido!")

def confirmar_saque():
    """Executa a operação de saque"""
    global saldo, numero_saques
    valor = entrada_valor.get()  # Obtém valor digitado
    try:
        valor = float(valor)  # Converte para número
        
        # Verifica restrições
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            messagebox.showerror("Erro", "Saldo insuficiente!")
        elif excedeu_limite:
            messagebox.showerror("Erro", f"Valor excede limite de {formatar_moeda(limite)} por saque")
        elif excedeu_saques:
            messagebox.showerror("Erro", f"Limite de {LIMITE_SAQUES} saques diários atingido!")
        elif valor > 0:  # Se todas as validações passarem
            saldo -= valor  # Atualiza saldo
            numero_saques += 1  # Incrementa contador
            registrar_transacao("Saque", valor)  # Registra transação
            messagebox.showinfo("Sucesso", f"Saque de {formatar_moeda(valor)} realizado!")
            esconder_campos_valor()  # Limpa interface
        else:
            messagebox.showerror("Erro", "Valor deve ser positivo!")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido!")

def ver_extrato():
    """Exibe o extrato com todas as transações"""
    cabecalho = "=============== EXTRATO ===============\n"
    rodape = f"\nSaldo: {formatar_moeda(saldo)}\n"
    rodape += "======================================="
    
    # Verifica se há transações
    if not extrato:
        mensagem = cabecalho + "Nenhuma transação realizada.\n" + rodape
    else:
        mensagem = cabecalho + extrato + rodape
    
    messagebox.showinfo("Extrato", mensagem)  # Exibe extrato

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela
janela.title("Sistema Bancário")  # Define título
janela.geometry("350x250")  # Define tamanho

# Configuração dos componentes de entrada
rotulo_valor = tk.Label(janela, text="Valor:")  # Rótulo
entrada_valor = tk.Entry(janela, validate="key",  # Campo de entrada
                        validatecommand=(janela.register(validar_entrada), "%P"))
botao_confirmar = tk.Button(janela, text="Confirmar")  # Botão de confirmação

# Criação dos botões de operação
tk.Button(janela, text="Depositar", command=depositar).pack(pady=5)
tk.Button(janela, text="Sacar", command=sacar).pack(pady=5)
tk.Button(janela, text="Extrato", command=ver_extrato).pack(pady=5)
tk.Button(janela, text="Sair", command=janela.quit).pack(pady=5)

# Inicia o loop principal da interface
janela.mainloop()