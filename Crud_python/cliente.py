class Cliente:

    def __init__(
        self,
        nome,
        email,
        telefone,
        id=None,
        data_cadastro=None
    ):

        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_cadastro = data_cadastro

    def __str__(self):

        return f"""
ID: {self.id}
Nome: {self.nome}
E-mail: {self.email}
Telefone: {self.telefone}
Cadastro: {self.data_cadastro}
-------------------------------
"""
