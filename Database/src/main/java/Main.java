import java.sql.Connection;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {

        System.out.println("Iniciando aplicação...");

        try (Connection conn = Database.conectar()) {

            System.out.println("Conexão com SQLite realizada!");
            System.out.println("Banco de dados smartweb.db inicializado!");
            System.out.println("Tabela users verificada com sucesso!");

        } catch (SQLException e) {

            System.out.println("Erro ao conectar com o banco de dados:");
            e.printStackTrace();

        }

        System.out.println("Aplicação finalizada.");
    }
}
