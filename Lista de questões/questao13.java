import java.util.Scanner;

public class questao13 {
    public static void main(String[] args) {
        Double somtotal;
        int totaltestes;
        Scanner entrada;
        entrada = new Scanner(System.in);

        totaltestes = 5;

        System.out.print("Insira a soma total: ");
        somtotal = entrada.nextDouble();

        for (int i = 1; i <= totaltestes; i++) {
            System.out.print("Digite o tempo de teste: " + i + " (em minutos): ");
        }

        double media = somtotal / totaltestes;

        System.out.print("Tempo Total: " + somtotal + "  min | Média: " + media + " min");
    }
}
