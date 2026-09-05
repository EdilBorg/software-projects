import Banco
import os
import usuario
import utilis
import categorias
import chamados
import ativos
Banco_dado = Banco.Banco_mysql()
Banco_dado.criar_tabela()


def menu(banco, email_usuario):
    os.system("clear")
    menu_inicial = ["Gestão de usuários", "Gestão de categorias", "Gestão de chamados",
                    "Gestão de ativos", "Atribuição de ativos", "Consultas e histórico",
                    "Relatórios"]
    while True:
        utilis.mostrar_dados_lista_enumerado(menu_inicial)
        print("[0]-Sair")
        opcao = utilis.validar_entrada("\nEscolha uma opcão valida: ", len(menu_inicial))

        if opcao == 1:
            estado_user = utilis.estado_usuario(banco, usuario, email_usuario)
            if not estado_user[0]:
                os.system("clear")
                print("usuario sem permisão\n")
                continue
            os.system("clear")
            print("Gestão de usuários\n".center(40))
            limite_opcao = utilis.gestao_usuarios()
            op = utilis.validar_entrada("Escolha uma opcão valida: ", limite_opcao)
            
            if op == 1:
                os.system("clear")
                print("Cadastro de usuários\n".center(40))
                dados = usuario.entrada_dado_usuario(utilis)
                confir = usuario.adicionar_usuarios(banco, dados['nome'], dados['email'], dados['tipo'])
                utilis.confirmacao(confir, "Usuario cadastrado com sucesso")

            elif op == 2:
                os.system("clear")
                print("Usuários Encontrados\n".center(40))
                todos_usuarios = usuario.mostrar_usuarios(banco, "*")
                if not todos_usuarios:
                    os.system("clear")
                    print("Nenhum usuario encontrado\n")
                    continue
                utilis.mostar_dado_banco(todos_usuarios)
            
            elif op == 3:
                print("em desenvolvimento")
            
            elif op == 4:
                os.system("clear")
                print("Editar\n".center(40))
                tabela = ['nome', 'email', 'tipo']
                utilis.mostrar_dados_lista_enumerado(tabela)
                opca = utilis.validar_entrada("Escolha uma opcão valida: ", 3)-1
                if tabela[opca] == "tipo":
                    os.system("clear")
                    novo = usuario.tipo_usuario(utilis)
                else:
                    novo = input(f"Novo {tabela[opca]}: ")
                if tabela[opca] == "nome":
                    novo.upper()
                saida = usuario.editar_usuarios(banco, tabela[opca],
                                        novo, input("Email do usuario:"))
                utilis.confirmacao(saida, f"{tabela[opca]} editado com sucesso")
            
            elif op == 5:
                os.system("clear")
                opcoes = ["Ativar", "Desativar"]
                print("Desativar\n".center(40))
                utilis.mostrar_dados_lista_enumerado(opcoes)
                escolha = utilis.validar_entrada("Escolha uma opcao valida: ", len(opcoes))-1
                if opcoes[escolha] == "Ativar":
                    novo = True
                    estado = "Ativado"
                else:
                    novo = False
                    estado = "Desativado"
                saida = usuario.editar_usuarios(banco, 'estado', novo, input("E-mail do usuario: "))
                utilis.confirmacao(saida, f"usuario {estado} com sucesso")
             
            elif op == 6:
                os.system("clear")
                print("Eliminar")
                conf = usuario.remover_usuarios(banco, input("Nome: "), input("E-mail: "))
                utilis.confirmacao(conf, "usuários eliminado com sucesso")
            elif op == 7:
                os.system("clear")
                continue            

        elif opcao == 2:
            estado_user = utilis.estado_usuario(banco, usuario, email_usuario)
            if not estado_user[0]:
                os.system("clear")
                print("usuario sem permisão\n")
                continue
            os.system("clear")
            limite_opcao = utilis.gestao_categorias()
            op = utilis.validar_entrada("Escolha uma opcão valida: ", limite_opcao)
            if op == 2:
                categorias.mostrar_categorias()

email = utilis.login(Banco_dado, usuario)
menu(Banco_dado, email)