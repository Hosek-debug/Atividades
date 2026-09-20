public class questao20 {
    public static void main(String[] args) {
        int anterior = 0;
        int atual = 1;
        int proximo;

        System.out.println("Os primeiros 15 termos da Sequência de Fibonacci:");

        for (int i = 1; i <= 15; i++) {
       
            System.out.print(anterior + " ");

            proximo = atual + anterior;
            anterior = atual;
            atual = proximo;
        }
    }
}
