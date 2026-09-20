import java.util.Scanner;

public class questao14 {
    public static void main(String[] args) {
        int opcao;
        Scanner entrada;
        entrada = new Scanner(System.in);

        do {
            System.out.print("-- Menu do sistema --");
            System.out.print("-- 1. Cadastrar --");
            System.out.print("-- 2. Consultar --");
            System.out.print("-- 3. Sair --");
            System.out.print("-- Escolha uma opção: --");

            opcao = entrada.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Cadastrando...");
                    break;
                case 2:
                    System.out.print("Consultando...");
                    break;
                case 3:
                    System.out.print("Saindo do sistema...");
                    break;
                default:
                    System.out.print("Opção inválida! Tente novamente.");
                    break;
            }            
        } while (opcao !=3);
    }
}
