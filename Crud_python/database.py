import mysql.connector
from config import Config


class Database:

    def __init__(self):
        self.config = Config()

    # Conectar ao servidor MySQL
    def conectar_servidor(self):

        return mysql.connector.connect(
            host=self.config.DB_HOST,
            port=self.config.DB_PORT,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD
        )

    # Conectar ao banco de dados
    def conectar(self):

        return mysql.connector.connect(
            host=self.config.DB_HOST,
            port=self.config.DB_PORT,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD,
            database=self.config.DB_NAME
        )

    # Criar database e tabela
    def inicializar_banco(self):

        conexao = None
        cursor = None

        try:
            conexao = self.conectar_servidor()
            cursor = conexao.cursor()

            nome_banco = self.config.DB_NAME

            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{nome_banco}` "
                "CHARACTER SET utf8mb4 "
                "COLLATE utf8mb4_unicode_ci"
            )

            print("Database verificada/criada!")

            cursor.execute(f"USE `{nome_banco}`")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL,
                    telefone VARCHAR(20),
                    data_cadastro TIMESTAMP
                        DEFAULT CURRENT_TIMESTAMP
                )
            """)

            print("Tabela clientes verificada/criada!")

        finally:

            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()
