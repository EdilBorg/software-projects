def adicionar_usuarios(banco, nome, email, tipo):
        try:
            banco.cursor.execute("""
                INSERT INTO usuarios(nome, email, tipo, estado)
                VALUES(%s,%s,%s, %s);
            """, (nome.upper(), email, tipo, True))
            banco.conexao.commit()
            return  True
        except Exception as erro:
            banco.conexao.rollback()
            return False

def remover_usuarios(banco, nome, email):
        banco.cursor.execute("""
            DELETE FROM usuarios WHERE nome = %s AND email = %s;
        """, (nome.upper(), email))
        banco.conexao.commit()
        return True

def editar_usuarios(banco, tipo_edit, dado_edit, email):
        colunas_permitidas = {'nome', 'email', 'tipo', 'estado'}
        if tipo_edit not in colunas_permitidas:
            return 0      
        banco.cursor.execute(f"""
            UPDATE usuarios SET {tipo_edit} = %s WHERE email = %s;
        """, (dado_edit, email))
        banco.conexao.commit()
        return True

def mostrar_usuarios(banco, coluna):
    try:
       banco.cursor.execute(f"SELECT {coluna} FROM usuarios")
       usuario_encontrados = banco.cursor.fetchall()
       return usuario_encontrados
    except:
          return False

def alterar_estado_usuario(banco, email, estado):
      banco.cursor.execute("""
          INSERT INTO usuarios(estado) WHERE email = %d
          VALUES(%d)
        """, (email, estado))

def tipo_usuario(utilis):
       cargo = ["ADMIN", "TECNICO", "ENG"]
       utilis.mostrar_dados_lista_enumerado(cargo)
       escolha = utilis.validar_entrada("\nEscolha uma opcão: ", len(cargo)) - 1
       return cargo[escolha]
  
def entrada_dado_usuario(utilis):
      usuario = {}
      usuario['nome'] = input("Nome: ")
      usuario['email'] = input("E-mail: ")
      tipo = tipo_usuario(utilis)
      usuario['tipo'] = tipo
      return usuario

def validar_usuario(banco, email):
        banco.cursor.execute("SELECT email FROM usuarios WHERE email = %s", (email, ))
        email_encontrado = banco.cursor.fetchone()
        return email_encontrado

def validar_estado(banco, email):
       banco.cursor.execute("SELECT estado FROM usuarios WHERE email = %s", (email, ))
       estado_encontrado = banco.cursor.fetchone()
       return estado_encontrado