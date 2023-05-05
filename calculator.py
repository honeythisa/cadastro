#Calculadora com Menu
op = 0
while(op!=5):
    print("Calculadora :)")
    print("1 - adição")
    print("2 - substração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair")

    op = int(input("Escolha a opção adequada: "))

    if(op==1):
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = n1 + n2
        print("Soma: ",soma)

    elif(op==2):
        nu1 = int(input("Digite o primeiro número: "))
        nu2 = int(input("Digite o segundo número: "))
        sub = nu1 - nu2
        print("Subtração: ", sub)

    elif(op==3):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        mult = num1 * num2
        print("Multiplicação: ", mult)

    elif(op==4):
        nume1 = float(input("Digite o primeiro número: "))
        nume2 = float(input("Digite o segundo número: "))
        divisao = nume1 / nume2
        print("Divisão: ", divisao)

    elif(op==5):
        print("Você escolheu SAIR da calculadora")

    else:
        print("Escolha o número da ação!!!!!")

print("programa encerrado")