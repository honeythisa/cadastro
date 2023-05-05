#A biblioteca tkinter é a responsável por criar elementos
#gráficos - tela, labels, botões. Nós iremos utilizar
#as classes e outros elementos existentes nessa
# biblioteca para construírmos nossa interface com o
# usuário.
import tkinter as tk
from tkinter import ttk

#Criando uma classe - um novo tipo de dados. No nosso caso a Classe
#tem o nome de Cliente e possuí quatro atributos(características)
#cpf,nome,idade,telefone.
class Cliente:
    #Método Construtor chamado __init__. É o método responsável por
    #reservar o espaço na memória no momento que uma variável(objeto
    #ou instância da classe) é criada. No nosso caso além dos quatro
    #atributos recebe como parâmetro o atributo self. Que faz referência
    #a variável que será criada.
    def __init__(self,cpf,nome,endereco,telefone,email,idade,especiePet,nomePet,trabalho):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.idade = idade
        self.especiePet = especiePet
        self.nomePet = nomePet
        self.trabalho = trabalho

#Criamos uma lista de Clientes Vazia - sem nenhum cliente
clientes = []
#O comando open abre um arquivo e lê o mesmo. O comando possui dois parametros
#Endereço do Arquivo no HD - C:/Users/29963905803/Documents/clientes.txt no
#nosso caso. E o segundo parametro indica o que poderemos fazer no arquivo
#No nosso caso o parâmetro é o "r" - que indica que apenas iremos ler o
#o arquivo
arquivo = open("C:/Users/melis/Documents/clientes.txt", "r")
contadorDelinha = 0
#Percorre todas as linhas do arquivo através do comando readlines()
for linha in arquivo.readlines():
    #Cada linha do nosso arquivo indica o nome de um cliente.
    #Dessa forma iremos acrescentar cada linha do arquivo na lista
    #de cliente atráves do comando Append
    #O arquivo traz consigo as quebras de linha. Por isso utilizamos
    # o comando strip para retirar as quebras de linha.
    if(contadorDelinha%8==0):
        cpf = linha.strip('\n')
    elif(contadorDelinha%8==1):
        nome = linha.strip('\n')
    elif(contadorDelinha%8==2):
        endereco = linha.strip('\n')
    elif(contadorDelinha%8==3):
        telefone = linha.strip('\n')
    elif (contadorDelinha%8==4):
        email = linha.strip('\n')
    elif (contadorDelinha%8==5):
        idade = linha.strip('\n')
    elif (contadorDelinha%8==6):
        especiePet = linha.strip('\n')
    elif (contadorDelinha%8==7):
        nomePet = linha.strip('\n')
    elif (contadorDelinha%8==8):
        trabalho = linha.strip('\n')

        novoCliente = Cliente(cpf,nome,endereco,telefone,email,idade,especiePet,nomePet,trabalho)
        clientes.append(novoCliente)
    contadorDelinha = contadorDelinha + 1
#Fecha o arquivo após extrair todos os dados nele existentes.
arquivo.close()

# Criando a janela
janela = tk.Tk()
# Configurando o título da janela
janela.title("Cadastro de Cliente - Pet shop")
# Configurando as dimensões da janela
janela.geometry("900x600")
# Adicionando um label na janela
labelCliente = tk.Label(janela, text="Clientes: ")
labelCliente.place(x=10,y=10)
#Adicionando um combo no cliente
vetorOpcoes = []
for i in  clientes:
    nome = i.nome
    vetorOpcoes.append(nome)
comboCliente = ttk.Combobox(janela,values=vetorOpcoes)
comboCliente.current()
comboCliente.place(x=110,y=10)
#Adicionando um combo no cliente
##vetorOpcoes = ["Masculino", "Feminino"]
##comboCliente = ttk.Combobox(janela,values=vetorOpcoes)
##comboCliente.current()
##comboCliente.place(x=110,y=10)
#Adicionando as informações referentes ao nome do Cliente
labelNome = tk.Label(janela, text="Nome: ")
labelNome.place(x=10,y=50)
textoNome = tk.Text(janela,width=50, height=1)
textoNome.place(x=110,y=50)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = tk.Label(janela, text="CPF:")
labelCPF.place(x=10, y=80)
textoCPF = tk.Text(janela,width=50, height=1)
textoCPF.place(x=110, y=80)
#Adicionando as informações referentes ao endereço do Cliente
labelEndereco = tk.Label(janela, text="Endereço:")
labelEndereco.place(x=10,y=110)
textoEndereco = tk.Text(janela,width=50,height=1)
textoEndereco.place(x=110, y=110)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = tk.Label(janela, text="Telefone:")
labelTelefone.place(x=10,y=140)
textoTelefone = tk.Text(janela,width=50,height=1)
textoTelefone.place(x=110,y=140)
#email
labelEmail = tk.Label(janela, text="Email:")
labelEmail.place(x=10,y=170)
textoEmail = tk.Text(janela,width=50,height=1)
textoEmail.place(x=110,y=170)
#idade
labelIdade = tk.Label(janela, text="Idade:")
labelIdade.place(x=10,y=200)
textoIdade = tk.Text(janela,width=50,height=1)
textoIdade.place(x=110,y=200)
#titulo
labelDadosPet = tk.Label(janela, text="DADOS DO PET", fg="white", bg="grey", font="Arial 15 bold italic")
labelDadosPet.place(x=10, y=250)
#especiePet
labelespeciePet = tk.Label(janela, text="Espécie do pet:")
labelespeciePet.place(x=10,y=300)
textoespeciePet = tk.Text(janela,width=50,height=1)
textoespeciePet.place(x=110,y=300)
#nomePet
labelnomePet = tk.Label(janela, text="Nome do pet:")
labelnomePet.place(x=10,y=330)
textonomePet = tk.Text(janela,width=50,height=1)
textonomePet.place(x=110,y=330)
#trabalho
labelTrabalho = tk.Label(janela, text="Tipo de trabalho:")
labelTrabalho.place(x=10,y=360)
textoTrabalho = tk.Text(janela,width=50,height=1)
textoTrabalho.place(x=110,y=360)
#Adicionando um botão a nossa tela
botaoInserir = tk.Button(janela, text="Inserir")
botaoInserir.place(x=50, y=400)
botaoApagar = tk.Button(janela, text="Apagar")
botaoApagar.place(x=150, y=400)
botaoAlterar = tk.Button(janela, text="Alterar")
botaoAlterar.place(x=250,y=400)
# Executando o loop principal da janela
janela.mainloop()