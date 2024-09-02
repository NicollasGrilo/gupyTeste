import java.util.Scanner;

public class Exercicio2 {

    public static boolean fibonacci(int n) {
        int a = 0, b = 1;
        
        while (a <= n) {
            if (a == n) {
                return true;
            }
            int soma = a + b;
            a = b;
            b = soma;
        }
        
        return false;
    }

    public static void main(String[] args) {
        Scanner inputData = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int numberData = inputData.nextInt();

        if (fibonacci(numberData)) {
            System.out.println("O número " + numberData + " pertence à sequência.");
        } else {
            System.out.println("O número " + numberData + " não pertence à sequência.");
        }
        
        inputData.close();
    }
}