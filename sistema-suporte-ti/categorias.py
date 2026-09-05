def adicionar_categorias(banco, nome):
    try:
        banco.cursor.execute("""
            INSERT INTO categorias(nome)
            VALUES(%s);
        """, (nome))
        banco.conexao.commit()
        return True
    except:
        banco.conexao.rollback()
        return False

def editar_categoria(banco, nome, nome_antigo):
    banco.cursor.execute("""
                        UPDATE categorias
                        SET nome = %s
                        WHERE nome = %s""",
                        (nome, nome_antigo))
    return True

def remover_categorias(banco, nome):
    banco.cursor.execute("DELETE FROM usuarios WHERE nome = %s", (nome))
    return True

def mostrar_categorias(banco):
    banco.cursor.execute("SELECT nome FROM categorias WHERE estado = True;")
    dado_encontrado = banco.cursor.fetchall()
    return dado_encontrado
