import utilis
def adicionar_ativos(banco, patrimonio, tipo, marca, modelo, numero_serie, estado, mysql):
    try:
        data = utilis.data_atual()
        banco.cursor.execute("""
            INSERT INT ativos(patrimonio, tipo, marca, modelo, numero_serie, estado, data)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
        """,(patrimonio, tipo, marca, modelo, numero_serie, estado, data))
        banco.conexao.commit()
        return True
    except mysql.connector.errors.IntegrityError:
        return "Erro ja existe esse item\n"

def editar_ativos(banco, marca, modelo, dado_editar, novo_dado):
    dado_editar_permitido = {"patrimonio", "tipo", "marca", "modelo", "numero_serie", " estado"}
    if dado_editar not in dado_editar_permitido:
        return False
    else:
        banco.cursor.execute(f"""
            UPDATE ativos SET {dado_editar} = %s
            WHERE marca = %s AND modelo = %s
        """, (novo_dado, marca, modelo))
        banco.conexao.commit()
        return True
    
def eliminar_ativos(banco, marca, modelo):
    banco.cursor.execute("DELETE FROM ativos WHERE marca = % AND modelo = %", (marca, modelo))
    banco.conexao.commit()
    return True

def mostrar_ativos(banco):
    banco.cursor.execute("SELECT * FROM ativos")
    ativos_encontrados = banco.cursor.fetchall()
    return ativos_encontrados

def gestao_ativos(utilis):
    ativo = ["Cadastrar", "Listar", "Pesquisar", "Editar", "Alterar estado"]
    utilis.mostrar_dados_lista_enumerado(ativo)
    return len(ativo)
