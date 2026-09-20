import java.util.Scanner;

public class questao16 {
    public static void main(String[] args) {
        int n;
        Scanner entrada;
        entrada = new Scanner(System.in);

        System.out.print("Insira um número");
        n = entrada.nextInt();

        if (n % 3 == 0 && n % 5 == 0) {
            System.out.println("FizzBuzz");
        }
        else if (n % 3 == 0) {
            System.out.println("Fizz");
        }
        else if (n % 5 == 0) {
            System.out.println("Buzz");
        }
        else {
            System.out.println(n);
        }
    }
}
