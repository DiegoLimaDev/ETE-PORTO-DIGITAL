import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Digite a quantidade máxima do produto:\n");
    int maxAmount = scanner.nextInt();
    System.out.println("Digite a quantidade mínima do produto:\n");
    int minAmount = scanner.nextInt();

    int productMedia = (maxAmount + minAmount) / 2;
    System.out.println("O estoque médio do produto é: " + productMedia);

  }

}