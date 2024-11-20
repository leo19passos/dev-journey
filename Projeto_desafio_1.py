def adicionar_contato():
    nome = input("Nome do contato: ")
    telefone = input("Telefone do contato: ")
    email = input("E-mail do contato: ")
    favorito = False
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    agenda.append(contato)
    print(f"O contato {nome} foi adicionado!")

def editar_contato():
    listar_contatos()
    try:
        indice = int(input("Indice do contato a ser editado: "))
        if  0<= indice < len(agenda):
            contato = agenda[indice]
            print("Deixe o campo vazio para não altera os dados do contato.")
            novo_nome = input(f"Novo nome ({contato['nome']}): ") or contato['nome']
            novo_telefone = input(f"novo telefone ({contato['telefone']}): ") or contato['telefone']
            novo_email = input(f"Novo E-mail do contato:({contato['email']}): ") or contato['email']
            contato.update({"nome":novo_nome, "telefone": novo_telefone, "email": novo_email})
            print("Contato atualizado com sucesso!")
        else:
            print("Digite um indice valido. tente novamente!")
    except ValueError:
        print("Digite um valor valido!")

def deletar_contato():
    listar_contatos()
    try:
        indice = int(input("Indice do contato a ser excluido: "))
        if 0 <= indice < len(agenda):
            contato = agenda.pop(indice)
            print(f"Contato {contato['nome']}, excluido.")
        else:
            print("Digite um indice valido!")
    except ValueError:
        print("Digite um valor valido!")
def favorito_contato():
    listar_contatos()
    try:
        indice = int(input("Indice do contato a ser favoritado: "))
        if 0 <= indice < len(agenda):
            contato = agenda[indice]
            contato ['favorito']= not contato ['favorito']
            status = "favorito" if contato['favorito'] else "não favorito!"
            print(f"contato {contato['nome']}  agora é  {status}")
        else:
            print("Digite um contato indice valido!")
    except ValueError:
        "Digite um valor valido!"

def listar_contatos():
    if not agenda:
        print("Agenda vazia! ")
        return
    else:
        for i, contato in enumerate(agenda):
            status = "❤" if contato ['favorito'] else ""
            print(f"{i}. {contato['nome']} ({contato['telefone']}, {contato['email']}) {status}")
def listar_favoritos():
    favoritos = [contato for contato in agenda if contato['favorito']]
    if not favoritos:
        print("Agenda de favoritos vazia! ")
        return
    else:
        for contato in favoritos:
           print(f"{contato['nome']} ({contato['telefone']}, {contato['email']}) ❤")

agenda=[]
while True:
    print("\n--------Agenda--------")
    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. deletar contato")
    print("4. Marcar como favorito")
    print("5. Listar todos os contatos")
    print("6. Listar todos os contatos favoritos")
    print("7. Sair do programa")


    escolha = (input("Escolha uma das opções: "))

    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        editar_contato()
    elif escolha == "3":
        deletar_contato()
    elif escolha == "4":
        favorito_contato()
    elif escolha == "5":
        listar_contatos()
    elif escolha == "6":
        listar_favoritos()
    elif escolha == "7":
        break







