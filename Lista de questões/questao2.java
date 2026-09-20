import java.util.Scanner;

public class questao2 {
    public static void main(String[] args) {
        String nome;
        Double n1, n2, n3;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("Insira seu nome ");
        nome = entrada.nextLine();

        System.out.print("insira a nota 1 ");
        n1 = entrada.nextDouble();

        System.out.print("Insira a nota 2 ");
        n2 = entrada.nextDouble();

        System.out.print("insira a nota 3 ");
        n3 = entrada.nextDouble();

        System.out.print("\n# A média do " + nome + " é " + ((n1 + n2 + n3) / 3));
    }
}
