menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

escolhas = ["d", "s", "e", "q"]
saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    escolha = input(f"Faça sua escolha: {menu}").lower()

    if escolha not in escolhas:
        print("Operação falhou! Operação inválida.")
        continue

    match escolha:
        case "d":
            try:
                valor = float(input("Informe o valor a ser depositado: "))
            except ValueError:
                print("Operação falhou! O valor informado é inválido. Por favor, digite um número.")
                continue 

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado para depósito é inválido. Deve ser um valor positivo.")

        case "s": 
            try:
                valor = float(input("Informe o valor a ser sacado: "))
            except ValueError:
                print("Operação falhou! O valor informado é inválido. Por favor, digite um número.")
                continue # Pula para a próxima iteração

            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Você excedeu o limite diário de saques.")
            elif valor <= 0:
                print("Operação falhou! O valor informado para saque é inválido. Deve ser um valor positivo.")
            elif valor > saldo:
                print("Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f} por transação.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        case "e":
            print("\n============= EXTRATO =============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("===================================")

        case "q":
            print("Obrigado por usar nosso sistema bancário. Volte sempre!")
            break