package questao6;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Qual valor do seu dia de trabalho?");
    double moneyPerDay = scanner.nextDouble();
    System.out.println("Quantos dias você trabalhou esse mês?");
    int days = scanner.nextInt();
    double total;
    if (days > 0 && days < 32) {
      total = days * moneyPerDay;
      System.out.println("O salário desse mês é: " + total);
    } else {
      System.out.println("Digite uma quantidade dias válidas.");
    }
  }

}
