import java.util.Scanner;

public class questao17 {
    public static void main(String[] args) {
        int numerosecreto = 42;
        int tentativas = 0;
        int palpite;
        Scanner entrada;
        entrada = new Scanner(System.in);

        System.out.print("--- Bem vindo ao jogo da advinhação ---");

        System.out.print("Digite seu palpite: ");
        palpite = entrada.nextInt();
        tentativas++;

        while (palpite != numerosecreto) {
            if (palpite > numerosecreto) {
                System.out.print("Muito alto! Tente novamente.");
            } else {
                System.out.print("Muito baixo! Tente novamente");
            }

            System.out.print("Diigte seu palpite: ");
            palpite = entrada.nextInt();
            tentativas++;

            break;
        }

        System.out.print("ACertou! Você  usou " + tentativas + " tentativas.");
    }
}
