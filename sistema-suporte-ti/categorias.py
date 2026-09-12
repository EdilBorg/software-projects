def adicionar_categorias(banco, nome, mysql):
    try:
        banco.cursor.execute("""
            INSERT INTO categorias(nome, estado)
            VALUES(%s, %s);
        """, (nome.title(), True))
        banco.conexao.commit()
        return True
    except mysql.connector.errors.IntegrityError:
        banco.conexao.rollback()
        return "Erro ja existe esse item na categoria\n"

def editar_categoria(banco, nome_antigo, nome):
    banco.cursor.execute("""
                        UPDATE categorias
                        SET nome = %s
                        WHERE nome = %s""",
                        (nome.title(), nome_antigo.title()))
    banco.conexao.commit()
    return True

def remover_categorias(banco, nome):
    banco.cursor.execute("DELETE FROM categorias WHERE nome = %s", (nome.title(), ))
    return True

def mostrar_categorias(banco):
    banco.cursor.execute("SELECT nome FROM categorias WHERE estado = %s;", (True, ))
    dado_encontrado = banco.cursor.fetchall()
    return dado_encontrado

def estado_categoria(banco, nome, estado):
    banco.cursor.execute("""
                         UPDATE categorias
                         SET estado = %s 
                         WHERE nome = %s;
                         """, 
                         (estado, nome.title()))
    banco.conexao.commit()
    return True

def gestao_categorias(utilis):
    categorias = ["Criar categorias", "Listar", "Editar categoria", "Eliminar", "Ativar/Desativar categoria", "Voltar"]
    utilis.mostrar_dados_lista_enumerado(categorias)
    return len(categorias)


