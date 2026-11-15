Projeto de Database para o grupo de POO.

Pessoa 2 - Conexão e inicialização do banco

O que tinha que fazer para o projeto:
Implementar o Database.java: conectar ao arquivo SQLite; ativar o pragma_foreign_keys = on, criar a tabela users;
fechar conexão e statement com try-with-resources.

Como executar o código?

Precisa instalar o MVN no computador, configurar para funcionar no Vscode;
Instalar as extensões do SQLite viewer e Maven for Java;
Abrir o terminal do Vscode, e digitar os códigos:
1) mvn clean compile
2) mvn exec:java "-Dexec.mainClass=Main"

