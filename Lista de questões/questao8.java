import java.util.Scanner;

public class questao8 {
    public static void main(String[] args) {
        int ppm;
        Scanner entrada;

        entrada = new Scanner(System.in);

        System.out.print("Insira o valor do PPM: ");
        ppm = entrada.nextInt();

        if (ppm <= 9) {
            System.out.print("Ar limpo, risco zero");
        } else if (ppm >= 10 && ppm <= 50) {
            System.out.print("Atençao: qualidade do ar moderado");
        } else {
            System.out.print("Alerta de emergência: evacuar o local");
        }
    }
}