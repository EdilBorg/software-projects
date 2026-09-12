import mysql.connector
import os
from dotenv  import load_dotenv
load_dotenv()

class Banco_mysql:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD")
        )
        self.cursor = self.conexao.cursor()

    def criar_banco_dado(self):
        estado = None   
        try:
            self.cursor.execute("CREATE DATABASE BANCO_NEXORA_IT;")
            self.cursor.execute("USE BANCO_NEXORA_IT;")
            estado = False
        except mysql.connector.errors.DatabaseError:
            estado = True
        self.cursor.execute("USE BANCO_NEXORA_IT;")
        return estado
    
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id int PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                tipo VARCHAR(100) NOT NULL,
                estado  BOOLEAN);
        """)

        self.cursor.execute("""
                INSERT IGNORE INTO usuarios(nome, email, estado)
                VALUES(%s, %s, %s);
        """, ("ADMIN", "admin@gmail.com", True))

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias(
                            id int PRIMARY KEY AUTO_INCREMENT,
                            nome VARCHAR(150) NOT NULL UNIQUE,
                            estado BOOLEAN);       
        """)

        self.cursor.execute("""
            INSERT IGNORE INTO categorias(nome, estado)
            VALUES('Hardware', True),
            ('Software', True),
            ('Rede', True),
            ('Acesso', True)
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS chamados(
                       id int PRIMARY KEY AUTO_INCREMENT,
                       titulo VARCHAR(120) NOT NULL,
                       usuario_id int,
                       categoria_id int,
                       prioridade VARCHAR(150),
                       estado VARCHAR(150),

                       FOREIGN KEY(usuario_id)
                        REFERENCES usuarios(id),

                       FOREIGN KEY(categoria_id)
                        REFERENCES categorias(id));
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ativos(
                            id int PRIMARY KEY AUTO_INCREMENT,
                            patrimonio VARCHAR(150) NOT NULL UNIQUE,
                            tipo VARCHAR(150) NOT NULL,
                            marca VARCHAR(150) NOT NULL,
                            modelo VARCHAR(150),
                            numero_serie VARCHAR(150) NOT NULL UNIQUE,
                            estado VARCHAR(150) NOT NULL,
                            data DATE NOT NULL);
        """)

        self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS atribuicoes(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            ativos_id INT,
                            usuario_id INT,
                            data_atribucoes DATE,
                            data_devolucao DATE,
                            estado VARCHAR(150) NOT NULL,
                            
                            FOREIGN KEY(ativos_id)
                                REFERENCES ativos(id),
                            
                            FOREIGN KEY(usuario_id)
                                REFERENCES usuarios(id));                       
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS comentarios(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            chamado_id INT,
                            usuario_id INT,
                            text  VARCHAR(200),
                            data_criacao DATE,

                            FOREIGN KEY(chamado_id)
                                REFERENCES chamados(id),
                            
                            FOREIGN KEY(usuario_id)
                               REFERENCES usuarios(id));
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico_chamados(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            chamado_id INT,
                            usuario_id INT,
                            acoes VARCHAR(150),
                            valor_anteriro VARCHAR(150),
                            novo_valor VARCHAR(150),
                            data_alteracao DATE,
                            
                            FOREIGN KEY(chamado_id)
                                REFERENCES chamados(id),
                            
                            FOREIGN KEY(usuario_id)
                               REFERENCES usuarios(id));
        """)