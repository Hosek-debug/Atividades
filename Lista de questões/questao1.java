import java.util.Scanner;
 
public class questao1 {
    public static void main(String[] args) {
        int x, y;
        Scanner entrada;
        // Estamos usamos o construtor Scanner para ler valores de entrada do teclado
 
        entrada = new Scanner(System.in);

        System.out.print("Insira o valor de X: ");
        x = entrada.nextInt();

        System.out.print("Insira o valor de Y: ");
        y = entrada.nextInt();

        System.out.print("\n# x + y = " + (x + y));

    }
}



