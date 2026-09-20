public class questao21 {
    public static void main(String[] args) {
        int[] leiturasensor = {45, 52, 30, 12, 88, 49, 71, 15, 65, 40};
        int totalanomalias = 0;
        
        for (int leitura : leiturasensor) {
            if (leitura > 50) {
                System.out.println("Anomalia detectada: " + leitura);
                totalanomalias++;
            }
        }
            System.out.println("Total de anomalias no sistema: " + totalanomalias);
    }
}
