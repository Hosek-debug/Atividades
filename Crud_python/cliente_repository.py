from mysql.connector import Error
from database import Database
from cliente import Cliente


class ClienteRepository:

    def __init__(self):
        self.database = Database()

    # CREATE - Cadastrar cliente
    def cadastrar(self, cliente):

        conexao = None
        cursor = None

        try:
            conexao = self.database.conectar()
            cursor = conexao.cursor()

            sql = """
                INSERT INTO clientes (nome, email, telefone)
                VALUES (%s, %s, %s)
            """

            valores = (
                cliente.nome,
                cliente.email,
                cliente.telefone
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Cliente cadastrado com sucesso!")
            return True

        except Error as erro:

            if conexao:
                conexao.rollback()

            print(f"Erro ao cadastrar: {erro}")
            return False

        finally:

            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()

    # READ - Listar clientes
    def listar(self):

        conexao = None
        cursor = None

        try:
            conexao = self.database.conectar()
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, nome, email, telefone, data_cadastro
                FROM clientes
                ORDER BY id
            """)

            registros = cursor.fetchall()

            clientes = []

            for registro in registros:

                cliente = Cliente(
                    id=registro[0],
                    nome=registro[1],
                    email=registro[2],
                    telefone=registro[3],
                    data_cadastro=registro[4]
                )

                clientes.append(cliente)

            return clientes

        except Error as erro:

            print(f"Erro ao consultar: {erro}")
            return []

        finally:

            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()

    # UPDATE - Atualizar cliente
    def atualizar(self, cliente):

        conexao = None
        cursor = None

        try:
            conexao = self.database.conectar()
            cursor = conexao.cursor()

            sql = """
                UPDATE clientes
                SET nome = %s,
                    email = %s,
                    telefone = %s
                WHERE id = %s
            """

            valores = (
                cliente.nome,
                cliente.email,
                cliente.telefone,
                cliente.id
            )

            cursor.execute(sql, valores)
            conexao.commit()

            if cursor.rowcount:
                print("Cliente atualizado com sucesso!")
                return True

            else:
                print("Cliente não encontrado ou sem alterações.")
                return False

        except Error as erro:

            if conexao:
                conexao.rollback()

            print(f"Erro ao atualizar: {erro}")
            return False

        finally:

            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()

    # DELETE - Excluir cliente
    def excluir(self, id_cliente):

        conexao = None
        cursor = None

        try:
            conexao = self.database.conectar()
            cursor = conexao.cursor()

            cursor.execute(
                "DELETE FROM clientes WHERE id = %s",
                (id_cliente,)
            )

            conexao.commit()

            if cursor.rowcount:
                print("Cliente excluído com sucesso!")
                return True

            else:
                print("Cliente não encontrado.")
                return False

        except Error as erro:

            if conexao:
                conexao.rollback()

            print(f"Erro ao excluir: {erro}")
            return False

        finally:

            if cursor:
                cursor.close()

            if conexao and conexao.is_connected():
                conexao.close()
