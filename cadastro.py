#A biblioteca tkinter é a responsável por criar elementos
#gráficos - tela, labels, botões. Nós iremos utilizar
#as classes e outros elementos existentes nessa
# biblioteca para construírmos nossa interface com o
# usuário.
from tkinter import *
from tkinter.ttk import Combobox


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
janela = Tk()
# Configurando o título da janela
janela.title("Cadastro de Cliente - Pet shop")
# Configurando as dimensões da janela
janela.geometry("900x600")
#adicionando imagem
#janela.wm_attributes("-transparentcolor", "grey")
#janela.overrideredirect(1)
##def move_app(e):
##    janela.geometry(f"+{e.x_tk}+{e.y_tk}")
frame_photo = PhotoImage(file="bg 1.png")
frame_label = Label(janela, border=0, bg="grey", image=frame_photo)
frame_label.pack()
#Adicionando um combo no cliente
##vetorOpcoes = ["Masculino", "Feminino"]
##comboCliente = tCombobox(janela,values=vetorOpcoes)
##comboCliente.current()
##comboCliente.place(x=110,y=10)
#Adicionando as informações referentes ao nome do Cliente
#label_fundo = Label(janela, )
#label_fundo.place (x=150, y=170)
# Adicionando um label na janela
labelbg = Label(janela, width=75, height=60)
labelbg.place(x=200,y=50)
#Adicionando um combo no cliente
labelCliente = Label(janela, text="Clientes: ")
labelCliente.place(x=200,y=80)
vetorOpcoes = []
for i in  clientes:
    nome = i.nome
    vetorOpcoes.append(nome)
comboCliente = Combobox(janela,values=vetorOpcoes)
comboCliente.current()
comboCliente.place(x=230,y=80)
labelNome = Label(janela, text="Nome: ")
labelNome.place(x=230,y=110)
textoNome = Text(janela,width=50, height=1)
textoNome.place(x=280,y=110)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = Label(janela, text="CPF:")
labelCPF.place(x=230, y=140)
textoCPF = Text(janela,width=50, height=1)
textoCPF.place(x=280, y=140)
#Adicionando as informações referentes ao endereço do Cliente
labelEndereco = Label(janela, text="Endereço:")
labelEndereco.place(x=230,y=170)
textoEndereco = Text(janela,width=50,height=1)
textoEndereco.place(x=280, y=170)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = Label(janela, text="Telefone:")
labelTelefone.place(x=230,y=200)
textoTelefone = Text(janela,width=50,height=1)
textoTelefone.place(x=280,y=200)
#email
labelEmail = Label(janela, text="Email:")
labelEmail.place(x=230,y=230)
textoEmail = Text(janela,width=50,height=1)
textoEmail.place(x=280,y=230)
#idade
labelIdade = Label(janela, text="Idade:")
labelIdade.place(x=230,y=260)
textoIdade = Text(janela,width=50,height=1)
textoIdade.place(x=280,y=260)
#titulo
labelDadosPet = Label(janela, text="DADOS DO PET", fg="white", bg="grey", font="Arial 15 bold italic")
labelDadosPet.place(x=230, y=310)
#especiePet
labelespeciePet = Label(janela, text="Espécie do pet:")
labelespeciePet.place(x=230,y=360)
textoespeciePet = Text(janela,width=50,height=1)
textoespeciePet.place(x=280,y=360)
#nomePet
labelnomePet = Label(janela, text="Nome do pet:")
labelnomePet.place(x=230,y=390)
textonomePet = Text(janela,width=50,height=1)
textonomePet.place(x=280,y=390)
#trabalho
labelTrabalho = Label(janela, text="Tipo de trabalho:")
labelTrabalho.place(x=230,y=420)
textoTrabalho = Text(janela,width=50,height=1)
textoTrabalho.place(x=280,y=420)
#Adicionando um botão a nossa tela
botaoInserir = Button(janela, text="Inserir")
botaoInserir.place(x=300, y=470)
botaoApagar = Button(janela, text="Apagar")
botaoApagar.place(x=400, y=470)
botaoAlterar = Button(janela, text="Alterar")
botaoAlterar.place(x=500,y=470)
# Executando o loop principal da janela
janela.mainloop()