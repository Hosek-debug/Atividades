from cliente import Cliente

class Menu:

    def __init__(self, repository):
        self.repository = repository

    # Menu principal
    def exibir(self):

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
                self.cadastrar()

            elif opcao == "2":
                self.listar()

            elif opcao == "3":
                self.atualizar()

            elif opcao == "4":
                self.excluir()

            elif opcao == "0":
                print("Sistema encerrado!")
                break

            else:
                print("Opção inválida!")

    # Cadastrar cliente
    def cadastrar(self):

        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").strip()

        if not nome or not email:
            print("Nome e e-mail são obrigatórios!")
            return

        cliente = Cliente(
            nome=nome,
            email=email,
            telefone=telefone
        )

        self.repository.cadastrar(cliente)

    # Listar clientes
    def listar(self):

        clientes = self.repository.listar()

        print("\n===== CLIENTES CADASTRADOS =====")

        if not clientes:
            print("Nenhum cliente encontrado.")
            return

        for cliente in clientes:
            print(cliente)

    # Atualizar cliente
    def atualizar(self):

        try:
            id_cliente = int(input("ID do cliente: "))

            nome = input("Novo nome: ").strip()
            email = input("Novo e-mail: ").strip()
            telefone = input("Novo telefone: ").strip()

            if not nome or not email:
                print("Nome e e-mail são obrigatórios!")
                return

            cliente = Cliente(
                id=id_cliente,
                nome=nome,
                email=email,
                telefone=telefone
            )

            self.repository.atualizar(cliente)

        except ValueError:
            print("Informe um ID numérico válido!")

    # Excluir cliente
    def excluir(self):

        try:
            id_cliente = int(input("ID do cliente: "))

            confirmar = input(
                "Confirma a exclusão? (s/n): "
            )

            if confirmar.lower() != "s":
                print("Exclusão cancelada.")
                return

            self.repository.excluir(id_cliente)

        except ValueError:
            print("Informe um ID numérico válido!")
