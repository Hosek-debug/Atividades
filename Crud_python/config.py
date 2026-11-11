import os
from dotenv import load_dotenv


class Config:

    def __init__(self):

        # Carregar variáveis do arquivo .env
        load_dotenv()

        self.DB_HOST = os.getenv("DB_HOST", "localhost")
        self.DB_PORT = int(os.getenv("DB_PORT", "3306"))
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_NAME = os.getenv("DB_NAME", "crud_python")

        self.validar_configuracoes()

    # Validar configurações
    def validar_configuracoes(self):

        obrigatorias = {
            "DB_USER": self.DB_USER,
            "DB_PASSWORD": self.DB_PASSWORD
        }

        faltando = [
            chave for chave, valor in obrigatorias.items()
            if valor is None
        ]

        if faltando:
            raise ValueError(
                f"Variáveis ausentes no .env: {', '.join(faltando)}"
            )

        if not self.DB_NAME.replace("_", "").isalnum():
            raise ValueError("Nome do banco de dados inválido.")

        if not 1 <= self.DB_PORT <= 65535:
            raise ValueError("Porta do MySQL inválida.")
