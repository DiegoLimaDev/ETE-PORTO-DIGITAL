package questao4;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println(
        "O preço promocional é do livro é de R$8,00 caso você compre até 10 livros. Fora do promoção o preço é R$12,00");
    System.out.println("Quantos livros você deseja?");
    int amount = scanner.nextInt();
    double price;
    if (amount <= 10) {
      price = amount * 8;
      System.out.println("O preço total é: " + price);
    } else {
      price = amount * 12;
      System.out.println("O preço total é: " + price);
    }

  }
}
