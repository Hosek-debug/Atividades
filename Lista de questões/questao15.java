import java.util.Scanner;

public class questao15 {
    public static void main(String[] args) {
        double temperatura;
        double maior = 100;
        double menor = 1;
        Scanner entrada;
        entrada = new Scanner(System.in);

        System.out.print("Digite as temperaturas (0 para parar): ");
        temperatura = entrada.nextDouble();

        while (true) {
            System.out.print("Temperatura: ");
            if (temperatura == 0) {
                break;
            }

            if (temperatura > maior) {
                maior = temperatura;
            }

            if (temperatura < menor) {
                menor = temperatura;
            }

            break;
        }

        System.out.print("Maior temperatura: " + maior);
        System.out.print("Menor temperatura: " + menor);
    }
}
