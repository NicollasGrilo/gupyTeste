import java.util.Scanner;

public class exercicio5 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a string à ser invertida: ");
        String inputData = scanner.nextLine();

        String invertida = inverterString(inputData);

        System.out.println("String invertida: " + invertida);

        scanner.close();
    }

    public static String inverterString(String str) {

        char[] caracteres = str.toCharArray();
        
        int inicioArray = 0;
        int fimArray = caracteres.length - 1;

        while (inicioArray < fimArray) {

            char temp = caracteres[inicioArray];
            caracteres[inicioArray] = caracteres[fimArray];
            caracteres[fimArray] = temp;
            
            inicioArray++;
            fimArray--;
        }
        
        return new String(caracteres);
    }
}