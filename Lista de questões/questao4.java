import java.util.Scanner;

public class questao4 {
    public static void main(String[] args) {
       Double n1, n2;
       Scanner entrada;

       entrada = new Scanner(System.in);

       System.out.print("insira a largura: ");
       n1 = entrada.nextDouble();

       System.out.print("Insira a comprimento: ");
       n2 = entrada.nextDouble();

       System.out.print("A área é: " + (n1 * n2));
       System.out.print("O perimetro é: " + ((n1 * 2) + (n2 * 2)));

    }
}