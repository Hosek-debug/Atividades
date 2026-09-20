import java.util.Scanner;

public class questao18 {
    public static void main(String[] args) {
        int numero;
        int divisores = 0;
        Scanner entrada;
        entrada = new Scanner(System.in);

        System.out.print("Insira um número inteiros positivo: ");
        numero = entrada.nextInt();

        for (int i = 1; i <= numero; i++) {
            if (numero % i == 0) {
                divisores++;
            }
        }

        if (divisores == 2) {
            System.out.print(numero + " é um número primo");
        } else {
            System.out.print(numero + " Nao é um número primo");
        }
    }
}
