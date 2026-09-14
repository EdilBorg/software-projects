import Banco
import os
import usuario
import utilis
import categorias
import chamados
import ativos
import mysql
Banco_dado = Banco.Banco_mysql()
estado = Banco_dado.criar_banco_dado()
Banco_dado.criar_tabela()


def menu(banco, email_usuario):
    menu_inicial = ["Gestão de usuários", "Gestão de categorias", "Gestão de chamados",
                    "Gestão de ativos", "Atribuição de ativos", "Consultas e histórico",
                    "Relatórios"]
    utilis.mensagem_tela()
    while True:
        utilis.mostrar_dados_lista_enumerado(menu_inicial)
        print("[0]-Sair")
        opcao = utilis.validar_entrada("\nEscolha uma opcão valida: ", len(menu_inicial))


#========================== USUARIOS ================================================
        if opcao == 1:
            estado_user = usuario.estado_usuario(banco, usuario, email_usuario)
            if not estado_user[0]:
                os.system("clear")
                print("usuario sem permisão\n")
                continue
            os.system("clear")
            print("Gestão de usuários\n".center(40))
            limite_opcao = usuario.gestao_usuarios(utilis)
            op = utilis.validar_entrada("Escolha uma opcão valida: ", limite_opcao)
            os.system("clear")

            if op == 1: # CADASTRAR USUARIO
                print("Cadastro de usuários\n".center(40))
                dados = usuario.entrada_dado_usuario(utilis)
                confir = usuario.adicionar_usuarios(banco, dados['nome'], dados['email'], dados['tipo'], mysql)
                utilis.confirmacao(confir, "Usuario cadastrado com sucesso")

            elif op == 2: # LISTAR USUARIOS
                nome_coluna_usuario = ["Id", "Nome", "G-mail", "Tipo", "Estado"]
                print("Usuários Encontrados\n".center(40))
                todos_usuarios = usuario.mostrar_usuarios(banco, "*")
                if not todos_usuarios:
                    print("Nenhum usuario encontrado\n")
                    continue
                utilis.mostar_dado_banco(todos_usuarios, nome_coluna_usuario)
            
            elif op == 3: # PESQUISAR USUARIO (NOME, EMAIL, ID)
                print("Pesquisa\n".center(40))
                tabela = ['nome', 'email', 'id']
                utilis.mostrar_dados_lista_enumerado(tabela)
                opca = utilis.validar_entrada("Escolha uma opcão valida: ", 3)-1
                if opca == 2: #PESQUISAR POR ID
                    pesquisa = utilis.validar_entrada(f"{tabela[opca]}: ", None)
                else:
                    pesquisa = input(f"{tabela[opca]}: ") #PESQUISAR POR EMAIL  OU NOME
                if tabela[opca] == 'nome': 
                    pesquisa.upper()
                pesquisa_encontrado = usuario.pesquisar_usuarios(banco, tabela[opca], pesquisa)
                utilis.mostar_dado_banco(pesquisa_encontrado)
            
            elif op == 4: # EDITAR USUARIO
                print("Editar\n".center(40))
                tabela = ['nome', 'email', 'tipo'] # DADOS PERMITIDOS PRA EDITAR
                utilis.mostrar_dados_lista_enumerado(tabela)
                opca = utilis.validar_entrada("Escolha uma opcão valida: ", 3)-1
                if tabela[opca] == "tipo":
                    os.system("clear")
                    novo = usuario.tipo_usuario(utilis) # EDITAR ESTADO (ATIVADO(1)/DESTIVADO(0))
                else:
                    novo = input(f"Novo {tabela[opca]}: ") # EDITAR NOME OU EMAIL
                if tabela[opca] == "nome":
                    novo.upper()
                saida = usuario.editar_usuarios(banco, tabela[opca],
                                        novo, input("Email do usuario:"))
                utilis.confirmacao(saida, f"{tabela[opca]} editado com sucesso")
            
            elif op == 5: # DESATIVAR ATIVAR USUARIO
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
             
            elif op == 6: # ELIMINAR USUARIO
                print("Eliminar\n".center(40))
                conf = usuario.remover_usuarios(banco, input("Nome: "), input("E-mail: "))
                utilis.confirmacao(conf, "usuários eliminado com sucesso")
            elif op == 7: # VOLTAR
                utilis.mensagem_tela()
                continue   


#=============================== CATEGORIAS ============================================
        elif opcao == 2:
            estado_user = usuario.estado_usuario(banco, usuario, email_usuario)
            if not estado_user[0]: # VERIFICAR PERMISAO DE USUARIO
                os.system("clear")
                print("usuario sem permisão\n")
                continue
            os.system("clear")
            print("Gestão de categorias\n".center(40))
            limite_opcao = categorias.gestao_categorias(utilis)
            op = utilis.validar_entrada("Escolha uma opcão valida: ", limite_opcao)
            os.system("clear")

            if op == 1: # CADASTRO DE CATEGORIAS
                print("Cadastro de Categoria\n".center(40))
                saida = categorias.adicionar_categorias(banco, input("Nome: "), mysql)
                utilis.confirmacao(saida, "Cadastro de Categoria Feito com sucesso")

            elif op == 2: # MOSTRAR TODAS AS CATEGORIAS DO BANCO
                categorias_encontrados = categorias.mostrar_categorias(banco)
                utilis.mostar_dado_banco(categorias_encontrados, [":"])

            elif op == 3: # EDITAR CATEGORIAS
                print("Editar Categoria\n".center(40))
                saida = categorias.editar_categoria(banco, input("Nome antigo: "), input("Novo Nome: "))
                utilis.confirmacao(saida, "Categoria editada com sucesso")

            elif op == 4: # ELIMINAR CATEGORIAS
                print("Eliminar\n".center(40))
                saida = categorias.remover_categorias(banco, input("Nome: "))
                utilis.confirmacao(saida, "Removido com sucesso")

            elif op == 5: # ATIVAR CATEGORIA PARA SER EXIBIDO NA TELA, E DESATIVAR PRA NAO SER EXIBIDO NA TELA
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
                saida = categorias.estado_categoria(banco, input("Nome: "), novo)
                utilis.confirmacao(saida, f"Categoria {estado} com sucesso")
            elif op == 6: # VOLTAR
                utilis.mensagem_tela()
                continue


#====================================== CHAMADOS ==============================================
        elif opcao == 3: # VERIFICAR PERMISAO DE USUARIO
            estado_user = usuario.estado_usuario(banco, usuario, email_usuario)
            if not estado_user[0]:
                os.system("clear")
                print("usuario sem permisão\n")
                continue
            os.system("clear")
            print("Gestão de chamados\n".center(40))
            limite_opcao = chamados.gestao_chamados(utilis) 
            op = utilis.validar_entrada("Escolha uma opcão valida: ", limite_opcao)
            os.system("clear")

            if op == 1: #CADASTRO CHAMADOS
                dado = chamados.entrada_dado_chamados(email_usuario, utilis)
                saida = chamados.adicionar_chamados(banco, dado['titulo'], dado['prioridade'],
                                                    dado['estado'], dado['categoria'], email_usuario)
                utilis.confirmacao(saida, "Cadastrado com sucesso")

            elif op == 2: # MOSTAR CHAMADOS
                nome_coluna_chamados = ["Titulo", "Categoria", "Prioridade", "Estado", "Usuarios"]
                dados_encontrados = chamados.mostar_todos_chamados(banco)
                utilis.mostar_dado_banco(dados_encontrados, nome_coluna_chamados)

            elif op == 3: # ALTERAR PRIORIDADE CHAMADOS
                nova_prioridade = chamados.prioridades_chamados(utilis)
                titulo = input("Titulo do chamado: ")
                categoria = input("Categoria: ")
                saida = chamados.editar_chamados(banco, nova_prioridade, "prioridade", titulo, categoria, email_usuario)
                utilis.confirmacao(saida, "Prioridade alterado com sucesso")
                
            elif op == 4: # RESOLVER  ESTADO CHAMADO
                estado = "Resolvido"
                titulo = input("Titulo: ")
                categoria = input("Categoria: ")
                saida = chamados.editar_chamados(banco, estado, "estado", titulo, categoria, email_usuario)
                utilis.confirmacao(saida, "Resolvido com sucesso")
            elif op == 5: # VOLTAR
                utilis.mensagem_tela()
                continue
            

#========================================== ATIVOS ======================================================
        elif opcao == 4:
            print()


utilis.primeiro_login(estado)
#email = utilis.login(Banco_dado, usuario)
menu(Banco_dado, 'admin@gmail.com')