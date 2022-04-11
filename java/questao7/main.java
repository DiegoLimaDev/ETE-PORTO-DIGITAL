package questao7;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Qual sua altura?");
    double height = scanner.nextDouble();
    double idealWeight = (72.7 * height) - 58;
    System.out.println("Seu peso ideal é: " + idealWeight);
  }

}
