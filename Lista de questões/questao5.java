import java.util.Scanner;

public class questao5 {
    public static void main(String[] args) {
        int n1, n2;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("insira o total de testes: ");
        n1 = entrada.nextInt();

        System.out.print("insira os testes com sucesso: ");
        n2 = entrada.nextInt();

        if (n1 > n2) {
            System.out.print("Os testes são maiores que os com sucessos");
        } else {
            System.out.print("Os testes com sucessos são maiores que os testes");
        }
    }
}
