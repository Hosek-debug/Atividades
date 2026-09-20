import java.util.Scanner;

public class questao7 {
    public static void main(String[] args) {
        Double n1;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("Insira sua nota final: ");
        n1 = entrada.nextDouble();

        if (n1 > 7.0) {
            System.out.print("Aprovado");
        } else if (n1 > 5.0) {
            System.out.print("Recuperaçao");
        } else {
            System.out.print("Reprovado");
        }
    }
}