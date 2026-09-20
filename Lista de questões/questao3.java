import java.util.Scanner;

public class questao3 {
    public static void main(String[] args) {
        Double c;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("Insira o valor do Celcius: ");
        c = entrada.nextDouble();

        System.out.print("O valor em Fahrenhait é " + ((c * 1.8) + 32));
    }
}