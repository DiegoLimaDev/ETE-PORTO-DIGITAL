package questão1;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Qual valor do seu depósito?");
    double dep = scanner.nextDouble();
    System.out.println("Por quanto meses você vai deixar esse valor depositado?");
    int meses = scanner.nextInt();
    int x = 1;
    while (x <= meses) {
      dep = dep + (dep * 0.05);
      x++;
    }
    System.out.println("O seu valor de resgate após " + meses + " meses é de: " + dep);
  }
}