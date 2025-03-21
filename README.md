# 🏦Sistema Bancário com Interface Gráfica🏦

Um sistema bancário simples desenvolvido em Python com interface gráfica usando a biblioteca Tkinter. O sistema permite realizar operações básicas como depósitos, saques e consultar o extrato.

---

## Funcionalidades

- **Depósito**: Adiciona um valor ao saldo da conta.
- **Saque**: Retira um valor do saldo da conta, respeitando o limite diário e o saldo disponível.
- **Extrato**: Exibe o histórico de transações e o saldo atual.
- **Interface Gráfica**: Interface amigável e intuitiva para interação com o usuário.

---

## Requisitos

- Python 3.x
- Biblioteca Tkinter (já incluída na instalação padrão do Python)
- Biblioteca `locale` (já incluída na instalação padrão do Python)

---

## Como Executar

1. **Clone o repositório e navegue até a pasta**:
   ```bash
   git clone https://github.com/rodr4g/sistema-bancario.git
   
   cd sistema-bancario
   
2. **Execute o script**:
   ```bash
   python sistema_bancario.py
   
3. **Utilize a interface gráfica**:
   - A interface será aberta em uma nova janela.
   - Use os botões para realizar depósitos, saques ou consultar o extrato.

---

## Estrutura do Código

  ### Variáveis Globais:
  `saldo`: Armazena o saldo atual da conta.
  
  `limite`: Define o valor máximo que pode ser sacado em uma única operação.
  
  `extrato`: Armazena o histórico de transações.
  
  `numero_saques`: Conta quantos saques foram realizados.
  
  `LIMITE_SAQUES`: Define o número máximo de saques permitidos.

---

  ### Funções:
  
  `depositar()`: Inicia o processo de depósito.
  
  `sacar()`: Inicia o processo de saque.
  
  `confirmar_deposito()`: Confirma e registra o depósito.
  
  `confirmar_saque()`: Confirma e registra o saque.
  
  `ver_extrato()`: Exibe o extrato com as movimentações e o saldo atual.
  
  `mostrar_campos_valor()`: Exibe os campos de valor e o botão "Confirmar".
  
  `esconder_campos_valor()`: Esconde os campos de valor e o botão "Confirmar".
  
  `validar_entrada()`: Valida se o valor digitado é um número positivo e fracionado.
  
  `formatar_moeda()`: Formata valores como moeda brasileira (R$ 0,00).

---

## Exemplo de Uso

 ### 1. Depósito

  - Clique em "Depositar".
  - Digite o valor desejado e clique em "Confirmar".
  - O valor será adicionado ao saldo e registrado no extrato.
    
 ### 2. Saque

  - Clique em "Sacar".
  - Digite o valor desejado e clique em "Confirmar".
  - O valor será subtraído do saldo e registrado no extrato, desde que respeite o limite diário e o saldo disponível.

 ### 3. Extrato
  - Clique em "Extrato".
  - O histórico de transações e o saldo atual serão exibidos.

---
### ⚙️Tecnologias

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---
