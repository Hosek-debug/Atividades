import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


# ==========================================
# CARREGAR VARIÁVEIS DO .ENV
# ==========================================

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "crud_python")


# ==========================================
# VALIDAR CONFIGURAÇÕES
# ==========================================

def validar_configuracoes():
    obrigatorias = {
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD
    }

    faltando = [
        chave for chave, valor in obrigatorias.items()
        if valor is None
    ]

    if faltando:
        raise ValueError(
            f"Variáveis ausentes no .env: {', '.join(faltando)}"
        )

    if not DB_NAME.replace("_", "").isalnum():
        raise ValueError("Nome do banco de dados inválido.")


# ==========================================
# CONECTAR AO SERVIDOR MYSQL
# ==========================================

def conectar_servidor():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )


# ==========================================
# CONECTAR AO BANCO DE DADOS
# ==========================================

def conectar():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# ==========================================
# CRIAR DATABASE E TABELA
# ==========================================

def inicializar_banco():
    conexao = None
    cursor = None

    try:
        conexao = conectar_servidor()
        cursor = conexao.cursor()

        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
            "CHARACTER SET utf8mb4 "
            "COLLATE utf8mb4_unicode_ci"
        )

        print("Database verificada/criada!")

        cursor.execute(f"USE `{DB_NAME}`")

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


# ==========================================
# CREATE - CADASTRAR
# ==========================================

def cadastrar():
    conexao = None
    cursor = None

    try:
        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").strip()

        if not nome or not email:
            print("Nome e e-mail são obrigatórios!")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO clientes (nome, email, telefone)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (nome, email, telefone))
        conexao.commit()

        print("Cliente cadastrado com sucesso!")

    except Error as erro:
        if conexao:
            conexao.rollback()
        print(f"Erro ao cadastrar: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================
# READ - LISTAR
# ==========================================

def listar():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, email, telefone, data_cadastro
            FROM clientes
            ORDER BY id
        """)

        clientes = cursor.fetchall()

        print("\n===== CLIENTES CADASTRADOS =====")

        if not clientes:
            print("Nenhum cliente encontrado.")

        for cliente in clientes:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
E-mail: {cliente[2]}
Telefone: {cliente[3]}
Cadastro: {cliente[4]}
-------------------------------
""")

    except Error as erro:
        print(f"Erro ao consultar: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================
# UPDATE - ATUALIZAR
# ==========================================

def atualizar():
    conexao = None
    cursor = None

    try:
        id_cliente = int(input("ID do cliente: "))
        nome = input("Novo nome: ").strip()
        email = input("Novo e-mail: ").strip()
        telefone = input("Novo telefone: ").strip()

        if not nome or not email:
            print("Nome e e-mail são obrigatórios!")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE clientes
            SET nome = %s,
                email = %s,
                telefone = %s
            WHERE id = %s
        """

        cursor.execute(
            sql,
            (nome, email, telefone, id_cliente)
        )

        conexao.commit()

        if cursor.rowcount:
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado ou sem alterações.")

    except ValueError:
        print("Informe um ID numérico válido!")

    except Error as erro:
        if conexao:
            conexao.rollback()
        print(f"Erro ao atualizar: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================
# DELETE - EXCLUIR
# ==========================================

def excluir():
    conexao = None
    cursor = None

    try:
        id_cliente = int(input("ID do cliente: "))

        confirmar = input(
            "Confirma a exclusão? (s/n): "
        )

        if confirmar.lower() != "s":
            print("Exclusão cancelada.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM clientes WHERE id = %s",
            (id_cliente,)
        )

        conexao.commit()

        if cursor.rowcount:
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    except ValueError:
        print("Informe um ID numérico válido!")

    except Error as erro:
        if conexao:
            conexao.rollback()
        print(f"Erro ao excluir: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():
    while True:
        print("""
================================
          SISTEMA CRUD
================================
1 - Cadastrar cliente
2 - Listar clientes
3 - Atualizar cliente
4 - Excluir cliente
0 - Sair
================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            atualizar()

        elif opcao == "4":
            excluir()

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


# ==========================================
# INICIALIZAÇÃO
# ==========================================

if __name__ == "__main__":
    try:
        validar_configuracoes()

        print("Inicializando sistema...")

        inicializar_banco()

        print("Sistema pronto!")

        menu()

    except (Error, ValueError) as erro:
        print(f"Falha ao iniciar o sistema: {erro}")


