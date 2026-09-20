import java.util.Scanner;

public class questao6 {
    public static void main(String[] args) {
        int numero;
        Scanner entrada;
        
        entrada = new Scanner(System.in);

        System.out.print("Insira o número: ");
        numero = entrada.nextInt();

        if (numero % 2 == 0) {
            System.out.print("O número " + numero + " par");
        } else {
            System.out.print("O número " + numero + " ímpar");
        }
    }
}