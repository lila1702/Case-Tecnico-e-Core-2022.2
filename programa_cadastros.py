def organizar_usuarios_idade(usuarios_db):
    for i in range(len(usuarios_db)):
        for j in range(len(usuarios_db)):
            # Organiza por idade primeiro
            if(usuarios_db[i][1] < usuarios_db[j][1]):
                # Troca-os de lugar
                usuarios_db[i], usuarios_db[j] = usuarios_db[j], usuarios_db[i]
            # Organiza alfabéticamente
            elif(usuarios_db[i][1] == usuarios_db[j][1]):
                if(usuarios_db[i][0] < usuarios_db[j][0]):
                    # Troca-os de lugar
                    usuarios_db[i], usuarios_db[j] = usuarios_db[j], usuarios_db[i]

def organizar_usuarios_nome(usuarios_db):
    for i in range(len(usuarios_db)):
        for j in range(len(usuarios_db)):
            # Organiza por nome primeiro
            if(usuarios_db[i][0] <= usuarios_db[j][0]):
                # Troca-os de lugar
                usuarios_db[i], usuarios_db[j] = usuarios_db[j], usuarios_db[i]
                # Organiza por idade
                if((usuarios_db[i][0] == usuarios_db[j][0]) and (usuarios_db[i][1] < usuarios_db[j][1])):
                    # Troca-os de lugar
                    usuarios_db[i], usuarios_db[j] = usuarios_db[j], usuarios_db[i]

def cadastrar_usuario(lista_usuarios):
    nome_usuario = input("\nDigite o nome do usuário: ")
    idade_usuario = input("Digite a idade do usuário: ")
    
    while(not idade_usuario.isnumeric()):
        idade_usuario = input("\nOps... A idade do usuário não é um número, tente novamente: ")
    
    # Obs: .title() padroniza os nomes da lista ao capitaliza-lo
    nome_usuario = nome_usuario.title()
    idade_usuario = int(idade_usuario)
    
    if(idade_usuario in range(0, 12)):
        categoria = "Criança"
    elif(idade_usuario in range(12, 20)):
        categoria = "Adolescente"
    elif(idade_usuario in range(20, 65)):
        categoria = "Adulto"
    else:
        categoria = "Idoso"
    
    lista_usuarios.append([nome_usuario, idade_usuario, categoria])
    
    print("\nUsuário Cadastrado com Sucesso!\n")

def visualizar_usuarios(usuarios_db):
    print("\n-----------Lista de Usuários:-----------")
    for i in range(len(usuarios_db)):
        print(f"{usuarios_db[i][0]} - {usuarios_db[i][1]} anos - {usuarios_db[i][2]}")
        
    print("-----------------------------------------\n")

# Principal
usuarios = []

# Mantém o programa rodando a menos que o usuário saia de propósito
while(True):
    print("-----------MENU-----------")
    print("[1] - Cadastrar Usuário")
    print("[2] - Visualizar Usuários (Priorizar ordem por idade)")
    print("[3] - Visualizar Usuários (Priorizar ordem por nome)")
    print("[0] - Sair do Programa")
    
    escolha_usuario = input("Digite selecione uma opção: ")
    if(escolha_usuario == "0"):
        break
    # Cadastro
    elif(escolha_usuario == "1"):
        cadastrar_usuario(usuarios)
    # Visualização
    elif(escolha_usuario == "2"):
        organizar_usuarios_idade(usuarios)
        visualizar_usuarios(usuarios)
    elif(escolha_usuario == "3"):
        organizar_usuarios_nome(usuarios)
        visualizar_usuarios(usuarios)