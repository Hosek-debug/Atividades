import java.util.Scanner;

public class questao10 {
    public static void main(String[] args) {
        int ano;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("Inisra o ano: ");
        ano = entrada.nextInt();

        if (( ano%400 == 0)|| (( ano%4 == 0 ) &&( ano%100 != 0))) {
            System.out.print(ano + "é um ano bissexto: ");
        } else {
            System.out.print("Nao é um ano bissexto: ");
        }
    }
}
