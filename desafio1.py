
menu = """
  ============= MENU =============>>

[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
   
Obrigado(a) por usar nosso serviços, \n tenha um bom dia!
Dúvidas ou sugestões entre em contato com nosso SAC,\n será um prazer atendê-lo(a)!
  ============= FIM! ===============>>        
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "2":
        valor = float(input("Informe o valor que você deseja depositar: "))

        if valor > 0:
            saldo += valor
            print("Sucesso! Seu depósito já está rendendo!\nTenha um bom dia.")
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha! Infelizmente valor o informado é inválido.")


    elif opcao == "1":
        valor = float(input("Informe o valor que você deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print("Falha! Infelizmente você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Falha! Infelizmente esse valor de saque excede seu limite.")

        elif excedeu_saques:
            print("Falha! Infelizmente seu número de saques de hoje excedeu.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha! Valor informado inválido.")

    elif opcao == "3":
        print("\n=*=*=*=*=*=*=* EXTRATO =*=*=*=*=*=*=*")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=*=*=*=*=*=*=*=* FIM! =*=*=*=*=*=*=*=*")

    elif opcao == "4":
        break

    else:
        print("Falha! Por gentileza selecione novamente a operação desejada.")
