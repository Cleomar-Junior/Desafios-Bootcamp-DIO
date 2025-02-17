saldo = 0.00
LIM_SAQUE = 500.00
SAQUES_DIARIO = 3
quantidade_saques = 0
extrato = ''

escolha = ''


while True:

    print(""" 
          [d] Depositar
          [s] Sacar
          [e] Extrato
          [f] Finalizar """)
    
    escolha = input("Escolha uma opção: ")    

    if escolha == 'd' or escolha == "D":
        deposito = input("Insira o valor a ser depositado: ")
        if deposito.isnumeric():
            deposito = float(deposito)
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
            else:
                print("Digite um valor maior que zero!")
        else:
            print("Insira um valor numérico")
        print(saldo)

    elif escolha == 's' or escolha == 'S':
        if quantidade_saques != SAQUES_DIARIO:
            saque = input("Insira o valor a ser sacado: ")
            try:
                saque = float(saque.replace(',', '.'))  
                if saque > saldo:
                    print("Você não tem saldo para sacar essa quantidade")
                    print(f"Seu saldo é R$ {saldo:.2f}")
                elif saque <= 0:
                    print("Você não pode sacar esse valor")
                elif saque > 500:
                    print("Só é permitido sacar 500 reais por vez.")
                else:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    quantidade_saques += 1
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            except ValueError:
                print("Valor inválido. Insira um valor numérico.")
        else:
            print("Limite de saques diários atingido.")

            
    elif escolha == 'e' or escolha == 'E':
        print("\n EXTRATO ")
        print("Não foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
    elif escolha == 'f' or escolha == 'F':
        break
    else:
        print("Insira uma opção válida")
            