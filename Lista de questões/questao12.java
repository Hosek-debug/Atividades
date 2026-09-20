import java.util.Scanner;

public class questao12 {
    public static void main(String[] args) {
        String senha;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("insira a senha: ");
        senha = entrada.nextLine();

        while (!senha.equals("admin123")) {
            System.out.print("Senha incorrerta, tente novamente");
            System.out.print("Digite a senha do sistema: ");
            senha = entrada.nextLine();
        }

        System.out.println("Acesso Liberado!");

    }
}
