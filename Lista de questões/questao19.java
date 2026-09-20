import java.util.Scanner;

public class questao19 {
    public static void main(String[] args) {
        double saldo = 100.0;
        int opcao;
        Scanner entrada;
        entrada = new Scanner(System.in);

        do {
            System.out.println("\n=== CAIXA ELETRÔNICO ===");
            System.out.println("Saldo atual: R$ " + saldo);
            System.out.println("1 - Depositar");
            System.out.println("2 - Sacar");
            System.out.println("3 - Sair");
            System.out.print("Escolha uma opção: ");
            
            opcao = entrada.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o valor para depósito: R$ ");
                    double valorDeposito = entrada.nextDouble();
                    
                    if (valorDeposito > 0) {
                        saldo += valorDeposito; 
                        System.out.println("Depósito realizado com sucesso!");
                    } else {
                        System.out.println("Valor inválido para depósito.");
                    }
                    break;

                case 2:
                    System.out.print("Digite o valor para saque: R$ ");
                    double valorSaque = entrada.nextDouble();
                    
                    if (valorSaque > saldo) {
                        System.out.println("Saldo Insuficiente!");
                    } else if (valorSaque <= 0) {
                        System.out.println("Valor inválido para saque.");
                    } else {
                        saldo -= valorSaque; 
                        System.out.println("Saque realizado com sucesso!");
                    }
                    break;

                case 3:
                    System.out.println("Saindo do sistema. Obrigado por utilizar nosso banco!");
                    break;

                default:
                    System.out.println("Opção inválida! Escolha 1, 2 ou 3.");
                    break;
            }

        } while (opcao != 3); {
        }
    }
}
