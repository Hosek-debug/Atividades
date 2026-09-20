import java.util.Scanner;

public class questao9 {
    public static void main(String[] args) {
        double num1, num2;
        Scanner entrada;

       entrada = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        num1 = entrada.nextDouble();

        System.out.print("Digite o segundo número: ");
        num2 = entrada.nextDouble();

        System.out.println("Escolha a operaçao:");
        System.out.println("1 - Somar");
        System.out.println("2 - Subtrair");
        System.out.println("3 - Multiplicar");
        System.out.println("4 - Dividir");
        System.out.print("Digite o número da opção desejada: ");
        int opcao = entrada.nextInt();

        switch (opcao) {
            case 1:
                double soma = num1 + num2;
                System.out.println("Resultado da Soma: " + soma);
                break;
            case 2:
                double subtracao = num1 - num2;
                System.out.println("Resultado da Subtraçao: " + subtracao);
                break;
            case 3:
                double multiplicacao = num1 * num2;
                System.out.println("Resultado da Multiplicaçao: " + multiplicacao);
                break;
            case 4:
 
                if (num2 == 0) {
                    System.out.println("Erro: Não é possível dividir por zero!");
                } else {
                    double divisao = num1 / num2;
                    System.out.println("Resultado da Divisao: " + divisao);
                }
                break;
            default:

                System.out.println("Opçao invalida! Escolha um número de 1 a 4.");
                break;
        }
    }
}