import os
import datetime
import utilis

def mensagem_tela():
    os.system("clear")
    mensagem_tela = "NEXORA SISTEMA DE SUPORTE TI\n".center(40)
    print(mensagem_tela)

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
                    print("opcao invalida\n")
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

#inacabado
def mostar_dado_banco(dados):
    #estados_usuario = ["Id", "Nome", "G-mail", "Estado"]
    if dados:
        for item in dados:
            for conteudo in item:
                print(conteudo, end=" ")
            print()
        input("\n[FECHAR]\nDigite qualquel tecla")
    else:
        print("Nenhum resultado encontrado\n")
    mensagem_tela()
    

def confirmacao(dado, mensagem):
    mensagem_tela()
    if type(dado) == str:
        print(dado)
    elif dado:
        print(f"{mensagem}!\n")
    else:
        print("Invalido\n")


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


def primeiro_login(dado):
    if not dado:
        mensagem_tela()
        print("""
            ==================================================
                            PRIMEIRO ACESSO
            ==================================================
              
              Esta é a conta administrativa inicial do sistema.

                Por segurança, recomendamos que altere os
                dados desta conta antes de continuar.

                Para alterar os dados:

                1. Acesse "Gestão de usuários"
                2. Escolha "Editar usuário"
                3. Selecione a conta  admin@gmail.com
                4. Altere os dados necessários

                Após realizar a alteração, continue utilizando
                o sistema normalmente.

                ==================================================

                Pressione ENTER para continuar...
        """)
        input()