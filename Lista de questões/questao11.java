import java.util.Scanner;

public class questao11 {
    public static void main(String[] args) {
        int numero;
        Scanner entrada;
        entrada = new Scanner(System.in);

        System.out.print("insira um número para a tabuada: ");
        numero = entrada.nextInt();
              
        for (int i = 1; i <= 10; ++i) 
            System.out.println(numero + " * " + i +
                               " = " + numero * i);
    }
}
