#Variável opção irá controlar o while que regula o menu. Inicialmente ele deve possuir qualquer valor diferente de 5,
#para que o menu seja executado pelo menos uma vez

opção = 0
#Variável que armazena a lista de clientes. Inicialmente acrescentamos 4 clientes na nossa lista:
#Rodrigo, Ricardo, Ana e Letícia
clientes = ["Rodrigo", "Ricardo", "Ana", "Letícia"]
#Inicio do Menu. O while regula o menu. Enquanto o usuário não digitar a opção 5. O programa irá ficar em execução.
while(opção!=5):
    #Sequencia de 6 comandos print que irão imprimir o menu enquanto o usuario não digitar a opção 5.
    print("Sistema do Supermercado")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3- Alterar Cliente")
    print("4 - Remover Cliente")
    print("5 - Sair")
    #Entrada de Dados. Neste ponto do programa o comando input irá ler através do teclado a opção que o usuário deseja executar.
    opção = int(input("Digite a opção desejada: "))
    #Estrutura Condicional que irá direcionar o programa para a opção escolhida do usuário.
    if(opção==1):
        #Opção realiza o cadastro do cliente
        print("Você escolheu a opção 1 - Cadastrar Cliente")
        #Leitura do nome do novo cliente via teclado através do comando input, o novo cliente ficará armazenado na variavel nome.
        nome = input("Entre com o nome do novo cliente: ")
        #O Comando append inclui um novo cliente(variável nome) na lista de clientes
        clientes.append(nome)
    elif(opção==2):
        #Opção realiza a çlistagem dos clientes cadastrados no supermercado.
        print("Você escolheu a opção 2 - Listar Clientes")
        #O Comando for irá percorrer a lista de clientes e o comando print irá imprimir cada um dos clientes cadastrados.
        for i in clientes:
            #Impressão de cada um dos clientes.
            print(i)
    elif(opção==3):
        #Opção que realiza a alteração do nome de um cliente já cadastrado.
        print("Você escolheu a opção 3 - Alterar Cliente")
        # Inicialmente o sistema imprime os clientes cadastrados para que o usuário possa escolher qual cliente irá remover.
        print("Clientes:")
        for i in clientes:
            print(i)
        #Pergunta ao usuário qual cliente ele deseja alterar.
        nome = input("Digite o nome do cliente que você deseja alterar: ")
        # Sabendo o cliente que queremos alterar iremos retirar o mesmo da lista de clientes.
        clientes.remove(nome)
        #Perguntar ao usuário o novo nome do cliente
        nome = input("Digite o novo nome do cliente: ")
        #Inserir o novo nome do cliente na lista de clientes.
        clientes.append(nome)
    elif(opção==4):
        #Opção que realiza a remoção de um cliente cadastrado
        print("Você escolheu a opção 4 - Remover Cliente")
        #Inicialmente o sistema imprime os clientes cadastrados para que o usuário possa escolher qual cliente irá remover.
        print("Clientes:")
        for i in clientes:
            print(i)
        #Após a impressão dos clientes cadastrados o Sistema pergunta o nome do cliente que será removido e armazena
        #o mesmo na variável nome
        nome = input("Entre com o nome do cliente que você quer remover: ")
        #O comando remove irá remover o nome da lista de clientes
        clientes.remove(nome)
    elif(opção==5):
        #Impressão da Saída do Sistema - após o usuário "escolher" a opção 5
        print("Você escolheu a opção 5 - Sair")
    else:
        #Impressão da mensagem de opção inválida. Caso o usuário digite um número fora do intervalo do menu(1 a 5).
        print("Você escolheu uma opção inválida")