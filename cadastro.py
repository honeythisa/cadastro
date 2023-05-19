#A biblioteca tkinter é a responsável por criar elementos
#gráficos - tela, labels, botões. Nós iremos utilizar
#as classes e outros elementos existentes nessa
# biblioteca para construírmos nossa interface com o
# usuário.
from tkinter import *
from tkinter.ttk import Combobox

def formatar_cpf(event):
    # Obtém o texto atual do Entry
    cpf = textoCPF.get()

    # Remove todos os caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Aplica a máscara do CPF (###.###.###-##)
    if len(cpf) >= 3:
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    elif len(cpf) >= 6:
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}'
    elif len(cpf) >= 9:
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}'
    elif len(cpf) > 0:
        cpf = f'{cpf[:3]}.{cpf[3:]}'

    # Atualiza o texto do Entry
    textoCPF.delete(0, END)
    textoCPF.insert(0, cpf)


def gravarArquivo():
    # Após a finalização do sistema pelo usuário. Ou seja após o usuário escolher
    # a opção 5, devemos gravar as informações no arquivo novamente.
    arquivo = open("C:/Users/melis/Documents/clientes.txt", "w")
    # Percorre a lista de clientes
    for i in clientes:
        # Acrescenta o cliente ao arquivo final
        arquivo.write(i.cpf + '\n')
        arquivo.write(i.nome + '\n')
        arquivo.write(i.endereco + '\n')
        arquivo.write(i.telefone + '\n')
        arquivo.write(i.email + '\n')
        arquivo.write(i.idade + '\n')
        arquivo.write(i.especiePet + '\n')
        arquivo.write(i.nomePet + '\n')
        arquivo.write(i.trabalho + '\n')
    # Fecha o Arquivo
    arquivo.close()
    janela.destroy()

def limparFormulario():
    textoNome.delete("1.0", "end")
    textoCPF.delete("1.0", "end")
    textoTelefone.delete("1.0", "end")
    textoEndereco.delete("1.0", "end")
    textoIdade.delete("1.0", "end")
    textoEmail.delete("1.0", "end")
    textoespeciePet.delete("1.0", "end")
    textonomePet.delete("1.0", "end")
    textoTrabalho.delete("1.0", "end")

def carregarClientes():
    for i in clientes:
        if(comboCliente.get()==i.nome):
            limparFormulario()
            textoNome.insert("1.0",i.nome)
            textoCPF.insert("1.0",i.cpf)
            textoTelefone.insert("1.0",i.telefone)
            textoEndereco.insert("1.0",i.endereco)
            textoIdade.insert("1.0", i.idade)
            textoEmail.insert("1.0", i.email)
            textoespeciePet.insert("1.0", i.especiePet)
            textonomePet.insert("1.0", i.nomePet)
            textoTrabalho.insert("1.0", i.trabalho)

def inserirClientes():
    novoCliente = Cliente(textoCPF.get("1.0","end-1c"),textoNome.get("1.0","end-1c"),textoEndereco.get("1.0","end-1c"),textoTelefone.get("1.0","end-1c"))
    clientes.append(novoCliente)
    # vetorOpcoes.append(novoCliente.nome)
    my_insert()
    limparFormulario()

def my_insert(): # adding data to Combobox
    #if e1.get() not in cb1['values']:
    comboCliente['values'] +=(textoNome.get("1.0","end-1c")) # add option

def remove_combo(): # removing option from the Combobox
    my_new=[] # Blank list to hold new values
    for opt in comboCliente['values']: # Loop through all options
        if(opt != comboCliente.get()):
            #print(opt)
            my_new.append(opt) # Add to new list
    comboCliente['values']=my_new # assign to new list
    comboCliente.delete(0,'end') # remove from current selection text
    comboCliente.current()

def apagarClientes():
    for cliente in clientes:
        if (comboCliente.get()==cliente.nome):
            clientes.remove(cliente)
            remove_combo()


def alterarClientes():
    print("inserirClientes")
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
labelbg = Label(janela, width=65, height=32, bg="light yellow")
labelbg.place(x=215,y=50)
#Adicionando um combo no cliente
labelCliente = Label(janela, text="Cliente: ", bg="light yellow")
labelCliente.place(x=230,y=80)
vetorOpcoes = []
for i in  clientes:
    nome = i.nome
    vetorOpcoes.append(nome)
comboCliente = Combobox(janela,values=vetorOpcoes)
comboCliente.current()
comboCliente.place(x=295,y=80)
botaoCarregar = Button(janela, text="Carregar", bg="light cyan",command=lambda:carregarClientes())
botaoCarregar.place(x=500, y=67)
labelNome = Label(janela, text="Nome: ",bg="light yellow")
labelNome.place(x=230,y=110)
textoNome = Text(janela,width=45, height=1)
textoNome.place(x=295,y=110)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = Label(janela, text="CPF:",bg="light yellow")
labelCPF.place(x=230, y=140)
textoCPF = Text(janela,width=45, height=1)
textoCPF.place(x=295, y=140)
#Adicionando as informações referentes ao endereço do Cliente
labelEndereco = Label(janela, text="Endereço:",bg="light yellow")
labelEndereco.place(x=230,y=170)
textoEndereco = Text(janela,width=45,height=1)
textoEndereco.place(x=295, y=170)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = Label(janela, text="Telefone:",bg="light yellow")
labelTelefone.place(x=230,y=200)
textoTelefone = Text(janela,width=45,height=1)
textoTelefone.place(x=295,y=200)
#email
labelEmail = Label(janela, text="Email:",bg="light yellow")
labelEmail.place(x=230,y=230)
textoEmail = Text(janela,width=45,height=1)
textoEmail.place(x=295,y=230)
#idade
labelIdade = Label(janela, text="Idade:",bg="light yellow")
labelIdade.place(x=230,y=260)
textoIdade = Text(janela,width=45,height=1)
textoIdade.place(x=295,y=260)
#titulo
labelDadosPet = Label(janela, text="DADOS DO PET", fg="white", bg="grey", font="Arial 15 bold italic")
labelDadosPet.place(x=230, y=310)
#especiePet
labelespeciePet = Label(janela, text="Espécie do pet:",bg="light yellow")
labelespeciePet.place(x=230,y=360)
textoespeciePet = Text(janela,width=42,height=1)
textoespeciePet.place(x=320,y=360)
#nomePet
labelnomePet = Label(janela, text="Nome do pet:",bg="light yellow")
labelnomePet.place(x=230,y=390)
textonomePet = Text(janela,width=42,height=1)
textonomePet.place(x=320,y=390)
#trabalho
labelTrabalho = Label(janela, text="Trabalho:",bg="light yellow")
labelTrabalho.place(x=230,y=420)
textoTrabalho = Text(janela,width=42,height=1)
textoTrabalho.place(x=320,y=420)
#Adicionando um botão a nossa tela
botaoInserir = Button(janela, text="Inserir", bg="light green",command=lambda:inserirClientes())
botaoInserir.place(x=330, y=470)
botaoApagar = Button(janela, text="Apagar", bg="light pink", command=lambda:apagarClientes())
botaoApagar.place(x=390, y=470)
botaoAlterar = Button(janela, text="Alterar", bg="light blue",command=lambda:alterarClientes(),)
botaoAlterar.place(x=450,y=470)
botaoSair = Button(janela, text="Sair", bg="light grey", command=lambda:gravarArquivo())
botaoSair.place(x=510,y=470)
# Executando o loop principal da janela
janela.mainloop()