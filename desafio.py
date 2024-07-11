# Menu de opções
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Inicio da operação
while True:
    opcao = input(menu)
# Operação de depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Extrato: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")

# Operação de saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! Voc~e não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Você excedeu seu limite.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu seu limite de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

# Operação de extrato
    elif opcao == "3":
        print("\n========== EXTRATRO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

# Comando para sair da operação
    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, por favor selecione navamente a operação desejada.")