import os
def estado_chamados(utilis):
    os.system("clear")
    print("Estados\n".center(40))
    estados = ["Aberto", "Em Atendimento", "Aguardando", "Resolvido", "Fechado",
               "Cancelado"]
    utilis.mostrar_dados_lista_enumerado(estados)
    escolha_estado = utilis.validar_entrada("Escolha uma opcao: ", len(estados))-1
    return estados[escolha_estado]

def prioridades_chamados(utilis):
    os.system("clear")
    print("Prioridade\n".center(40))
    prioridades = ["Baixa", "Normal", "Critica", "Alta".title()]
    utilis.mostrar_dados_lista_enumerado(prioridades)
    escolha_prioridade = utilis.validar_entrada("Escolha uma opcao: ", len(prioridades))-1
    return prioridades[escolha_prioridade]
    
def levar_id(banco, categoria_id, email):
    try:
        if not email:
            banco.cursor.execute(f"SELECT id FROM categorias WHERE nome = %s;", (categoria_id, ))
            id = banco.cursor.fetchone()
            return id[0]
        else:
            banco.cursor.execute(f"SELECT id FROM usuarios WHERE email = %s;", (email, ))
            id = banco.cursor.fetchone()
            return id[0]
    except:
        banco.conexao.rollback()
        return False

def adicionar_chamados(banco, titulo, prioridade, estado, tipo_problema, email_usuario):
    try:
        id_categoria = levar_id(banco, tipo_problema.title(), "")
        id_usuario = levar_id(banco, "", email_usuario)
        banco.cursor.execute("""
            INSERT INTO chamados(titulo, usuario_id, categoria_id, prioridade, estado)
            VALUES(%s, %s, %s, %s, %s);
        """, (titulo, id_usuario, id_categoria, prioridade, estado))
        banco.conexao.commit()
        return True
    except:
        banco.conexao.rollback()
        return False

def editar_chamados(banco, dado_editar, coluna, titulo, categoria, usuario):
    coluna_permitidos = {"titulo", "prioridade", "estado"}
    id_usuario = levar_id(banco, "", usuario)
    id_categoria = levar_id(banco, categoria.title(), "")
    if coluna  not in coluna_permitidos:
        return False
    banco.cursor.execute(f"""
        UPDATE chamados SET {coluna} = %s, usuario_id = %s WHERE titulo = %s AND categoria_id = %s;
    """, (dado_editar, id_usuario, titulo, id_categoria))
    banco.conexao.commit()
    return True

def eliminar_chamados(banco, titulo, email):
    email_id = levar_id(banco, "", email)
    banco.cursor.execute("DELETE FROM chamados WHERE titulo = %s AND usuario_id = %s;",
                         (titulo, email_id))
    banco.conexao.commit()
    return True

def mostar_todos_chamados(banco):
    banco.cursor.execute("""
        SELECT chamados.titulo, categorias.nome,
        chamados.prioridade, chamados.estado, usuarios.nome
        FROM usuarios
        JOIN chamados
        ON usuarios.id = chamados.usuario_id
        JOIN categorias
        ON categorias.id = chamados.categoria_id ;
    """)
    dados_encontrados = banco.cursor.fetchall()
    return dados_encontrados

def gestao_chamados(utilis):
    chamados = ["Criar", "Mostrar todos chamados", "Alterar prioridade", "Resolver", "Sair"]
    utilis.mostrar_dados_lista_enumerado(chamados)
    return len(chamados)

def entrada_dado_chamados(usuario_ativo, utilis):
    chamados = {}
    chamados['titulo'] = input("Titulo: ")
    chamados['categoria'] = input("Categoria: ").title()
    chamados['prioridade'] = prioridades_chamados(utilis)
    chamados['estado'] = estado_chamados(utilis)
    return chamados