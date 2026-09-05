import os
import datetime

def data_atual():
    data = datetime.datetime.now().date()
    return data

def data_prolongada(dia):
    data_agora = data_atual()
    data_nova = data_agora + datetime.timedelta(dia)
    return data_nova

def validar_entrada(mensagem, limite_entrada):
    while True:
        try:
            op = int(input(mensagem ))
            if not limite_entrada:
                return op
            else:
                if op > limite_entrada or op < 0:
                    print("opcao invalida")
                    continue
                else:
                    return op
        except ValueError:
            os.system("clear")
            print("Entrada Ivalida\n")
            continue

def mostrar_dados_lista_enumerado(dados):
    for n, item in enumerate(dados, start=1):
        print(f"[{n}]-{item}")

def mostar_dado_banco(dados):
    for item in dados:
        for n in item:
            print(n, end=" ")
        print()
    input("\n[FECHAR]\nDigite qualquel tecla")
    os.system("clear")
    

def gestao_usuarios():
    opcoes_usuario = ["Cadastrar", "Listar", "Pesquisar", "Editar", "Desativar/Ativar", "Eliminar", "Voltar"]
    mostrar_dados_lista_enumerado(opcoes_usuario)
    return len(opcoes_usuario)

def gestao_categorias():
    categorias = ["Criar categorias", "Listar", "pesquisar", "editar categoria", "Desativar categoria", "Voltar"]
    mostrar_dados_lista_enumerado(categorias)
    return len(categorias)

def gestao_chamados():
    chamados = ["Criar", "Consultar fila", "Alterar prioridade", "Resolver"]
    mostrar_dados_lista_enumerado(chamados)
    return len(chamados)

def confirmacao(dado, mensagem):
    os.system("clear")
    if dado:
        print(f"{mensagem}!\n")
    else:
        print("Invalido")


def login(banco, usuario):
    while True:
        os.system("clear")
        print("Login\n".center(40))
        email = input("E-mail: ")
        saida = usuario.validar_usuario(banco, email)
        if saida:
            return email
        else:
            os.system("clear")
            print("usuario invalido")
            continue

def estado_usuario(banco, usuario, email):
    saida_estado = usuario.validar_estado(banco, email)
    return saida_estado