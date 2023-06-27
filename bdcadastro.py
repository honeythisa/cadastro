from tkinter import *
from tkinter.ttk import Combobox
import mysql.connector
from tkinter import messagebox


def formatar_cpf(event):
    # Obtém o texto atual do Entry

    cpf = cpf.get()

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
    cpf.delete(0, END)
    cpf.insert(0, cpf)


# Conectar ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="aluno",
    database="petShop"
)
# Criar a tabela de clientes
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), "
               "endereco VARCHAR(255), cpf VARCHAR(11), telefone VARCHAR(11), email VARCHAR(30), idade VARCHAR(4), "
               "especiePet VARCHAR(255), nomePet VARCHAR(255), trabalho VARCHAR(255))")

cursor = db.cursor()
cursor.execute("SELECT nome FROM clientes")
clientes = cursor.fetchall()
print("Clientes:", clientes)


def atualizarCombo():
    # Carregar os clientes no ComboBox
    cursor = db.cursor()
    cursor.execute("SELECT nome FROM clientes")
    clientes = cursor.fetchall()
    clientesLista = []
    for i in clientes:
        clientesLista.append(i[0])
    print(clientesLista)
    combo_clientes["values"] = clientesLista


def adicionar_cliente():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    idade = entry_idade.get()
    especiePet = entry_especiePet.get()
    nomePet = entry_nomePet.get()
    trabalho = entry_trabalho.get()

    cursor = db.cursor()
    sql = "INSERT INTO clientes (nome, endereco, cpf, telefone, email, idade, especiePet, nomePet, trabalho) VALUES (" \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nome, endereco, cpf, telefone, email, idade, especiePet, nomePet, trabalho)
    cursor.execute(sql, val)
    db.commit()

    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso.")

    entry_nome.delete(0, END)
    entry_endereco.delete(0, END)
    entry_cpf.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)
    entry_idade.delete(0, END)
    entry_especiePet.delete(0, END)
    entry_nomePet.delete(0, END)
    entry_trabalho.delete(0, END)
    atualizarCombo()


def atualizar_cliente():
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        messagebox.showerror("Erro", "Por favor, selecione um cliente para atualizar.")
        return

    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    idade = entry_idade.get()
    especiePet = entry_especiePet.get()
    nomePet = entry_nomePet.get()
    trabalho = entry_trabalho.get()

    if nome == "" or endereco == "" or cpf == "" or telefone == "" or email == "" or idade == "" or especiePet == "" or nomePet == "" or trabalho == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    cursor = db.cursor()
    sql = "UPDATE clientes SET nome = %s, endereco = %s, cpf = %s, telefone = %s, email = %s, idade = %s, especiePet " \
          "= %s, nomePet = %s, trabalho = %s WHERE nome = %s"
    val = (nome, endereco, cpf, telefone, email, idade, especiePet, nomePet, trabalho, cliente_selecionado)
    cursor.execute(sql, val)
    db.commit()

    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso.")

    entry_nome.delete(0, END)
    entry_endereco.delete(0, END)
    entry_cpf.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)
    entry_idade.delete(0, END)
    entry_especiePet.delete(0, END)
    entry_nomePet.delete(0, END)
    entry_trabalho.delete(0, END)
    combo_clientes.set("")
    atualizarCombo()


def deletar_cliente():
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        messagebox.showerror("Erro", "Por favor, selecione um cliente para deletar.")
        return

    if messagebox.askyesno("Confirmação", f"Tem certeza que deseja deletar o cliente {cliente_selecionado}?"):
        cursor = db.cursor()
        sql = "DELETE FROM clientes WHERE nome = %s"
        val = (cliente_selecionado,)
        cursor.execute(sql, val)
        db.commit()

        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso.")

        entry_nome.delete(0, END)
        entry_endereco.delete(0, END)
        entry_cpf.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_idade.delete(0, END)
        entry_especiePet.delete(0, END)
        entry_nomePet.delete(0, END)
        entry_trabalho.delete(0, END)
        combo_clientes.set("")

    atualizarCombo()


def selecionar_cliente(event):
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        entry_nome.delete(0, END)
        entry_endereco.delete(0, END)
        entry_cpf.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_idade.delete(0, END)
        entry_especiePet.delete(0, END)
        entry_nomePet.delete(0, END)
        entry_trabalho.delete(0, END)
        return

    cursor = db.cursor()
    sql = "SELECT * FROM clientes WHERE nome = %s"
    val = (cliente_selecionado,)
    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    entry_nome.delete(0, END)
    entry_endereco.delete(0, END)
    entry_cpf.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)
    entry_idade.delete(0, END)
    entry_especiePet.delete(0, END)
    entry_nomePet.delete(0, END)
    entry_trabalho.delete(0, END)

    if resultado:
        entry_nome.insert(END, resultado[1])
        entry_endereco.insert(END, resultado[2])
        entry_cpf.insert(END, resultado[3])
        entry_telefone.insert(END, resultado[4])
        entry_email.insert(END, resultado[5])
        entry_idade.insert(END, resultado[6])
        entry_especiePet.insert(END, resultado[7])
        entry_nomePet.insert(END, resultado[8])
        entry_trabalho.insert(END, resultado[9])

def limparFormulario():
    entry_nome.delete(0, END)
    entry_endereco.delete(0, END)
    entry_cpf.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)
    entry_idade.delete(0, END)
    entry_especiePet.delete(0, END)
    entry_nomePet.delete(0, END)
    entry_trabalho.delete(0, END)


# Criar a janela principal
window = Tk()
window.title("PET SHOP")
window.geometry("900x600")
frame_photo = PhotoImage(file="bg 1.png")
frame_label = Label(window, border=0, bg="grey", image=frame_photo)
frame_label.pack()
labelbg = Label(window, width=65, height=32, bg="light yellow")
labelbg.place(x=215, y=50)
# Criar os campos de entrada e rótulos
label_nome = Label(window, text="Nome cliente:", bg="light yellow")
# label_nome = Text(window,width=45, height=1)
label_nome.place(x=230, y=110)
entry_nome = Entry(window)
entry_nome.place(x=320, y=110, width=340)

# Adicionando as informações referentes ao CPF do Cliente
labelcpf = Label(window, text="CPF:", bg="light yellow")
labelcpf.place(x=230, y=140)
entry_cpf = Entry(window)
entry_cpf.place(x=295, y=140, width=365)
# Adicionando as informações referentes ao
# endereço do Cliente
labelEndereco = Label(window, text="Endereço:", bg="light yellow")
labelEndereco.place(x=230, y=170)
entry_endereco = Entry(window)
entry_endereco.place(x=295, y=170, width=365)
# Adicionando as informações referentes ao telefone do Cliente
labelTelefone = Label(window, text="Telefone:", bg="light yellow")
labelTelefone.place(x=230, y=200)
entry_telefone = Entry(window)
entry_telefone.place(x=295, y=200, width=365)
# email
labelEmail = Label(window, text="Email:", bg="light yellow")
labelEmail.place(x=230, y=230)
entry_email = Entry(window)
entry_email.place(x=295, y=230, width=365)
# idade
labelIdade = Label(window, text="Idade:", bg="light yellow")
labelIdade.place(x=230, y=260)
entry_idade = Entry(window)
entry_idade.place(x=295, y=260, width=365)
# titulo
labelDadosPet = Label(window, text="DADOS DO PET", fg="white", bg="grey", font="Arial 15 bold italic")
labelDadosPet.place(x=230, y=310)
# especiePet
labelespeciePet = Label(window, text="Espécie do pet:", bg="light yellow")
labelespeciePet.place(x=230, y=360)
entry_especiePet = Entry(window)
entry_especiePet.place(x=320, y=360, width=340)
# nomePet
labelnomePet = Label(window, text="Nome do pet:", bg="light yellow")
labelnomePet.place(x=230, y=390)
entry_nomePet = Entry(window)
entry_nomePet.place(x=320, y=390, width=340)
# trabalho
labelTrabalho = Label(window, text="Trabalho:", bg="light yellow")
labelTrabalho.place(x=230, y=420)
entry_trabalho = Entry(window)
entry_trabalho.place(x=320, y=420, width=340)
# Adicionando um botão a nossa tela
##botaoInserir = Button(window, text="Inserir", bg="light green",command=lambda:inserirClientes())
##botaoInserir.place(x=330, y=470)
##botaoApagar = Button(window, text="Apagar", bg="light pink", command=lambda:apagarClientes())
##botaoApagar.place(x=390, y=470)
##botaoAlterar = Button(window, text="Alterar", bg="light blue",command=lambda:alterarClientes(),)
##botaoAlterar.place(x=450,y=470)
##botaoSair = Button(window, text="Sair", bg="light grey", command=lambda:gravarArquivo())
##botaoSair.place(x=510,y=470)

# Criar o botão "Adicionar"
button_adicionar = Button(window, text="Adicionar", bg="light green", command=adicionar_cliente)
button_adicionar.place(x=320, y=470)

# Criar o botão "Atualizar"
button_atualizar = Button(window, text="Atualizar", bg="light blue", command=atualizar_cliente)
button_atualizar.place(x=420, y=470)

# Criar o botão "Deletar"
button_deletar = Button(window, text="Deletar", bg="light pink", command=deletar_cliente)
button_deletar.place(x=520, y=470)
# Criar o ComboBox para selecionar o cliente
label_cliente = Label(window, text="Cliente:", bg="light yellow")
label_cliente.place(x=230, y=80)
combo_clientes = Combobox(window)
combo_clientes.place(x=295, y=80)
combo_clientes.bind("<<ComboboxSelected>>", selecionar_cliente)
#Limpar formulario
button_limpar = Button(window, text="Limpar formulário", bg="light cyan", command=limparFormulario)
button_limpar.place(x=500, y=67)

atualizarCombo()

# Iniciar a interface da aplicação
window.mainloop()
