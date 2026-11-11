from mysql.connector import Error
from config import Config
from database import Database
from cliente_repository import ClienteRepository
from menu import Menu


def main():

    try:

        print("Inicializando sistema...")

        # Validar configurações
        config = Config()

        print("Configurações verificadas!")

        # Inicializar banco de dados
        database = Database()
        database.inicializar_banco()

        print("Sistema pronto!")

        # Criar repositório
        repository = ClienteRepository()

        # Criar menu
        menu = Menu(repository)

        # Iniciar sistema
        menu.exibir()

    except (Error, ValueError) as erro:

        print(f"Falha ao iniciar o sistema: {erro}")


if __name__ == "__main__":
    main()
