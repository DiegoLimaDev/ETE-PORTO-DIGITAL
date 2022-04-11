package questao3;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println(
        "Segue o cardápio:\nCachorro quente R$1,20 (código:101)\nBauru simples R$1,30 (código:102)\nBauru com ovo R$1,50 (código:103)\nHambúrguer R$1,20 (código:104)\nChesseburguer R$1,30 (código:105)\nRefrigerante R$1,00 (código:106)");
    System.out.println("Qual o código do seu pedido?");
    int code = scanner.nextInt();
    double price;
    if (code == 101 || code == 104) {
      System.out.println("Quantos você deseja?");
      int amount = scanner.nextInt();
      price = amount * 1.20;
      System.out.println("O valor total é: " + price);
    } else if (code == 102 || code == 105) {
      System.out.println("Quantos você deseja?");
      int amount = scanner.nextInt();
      price = amount * 1.30;
      System.out.println("O valor total é: " + price);
    } else if (code == 103) {
      System.out.println("Quantos você deseja?");
      int amount = scanner.nextInt();
      price = amount * 1.50;
      System.out.println("O valor total é: " + price);
    } else if (code == 106) {
      System.out.println("Quantos você deseja?");
      int amount = scanner.nextInt();
      price = amount * 1.00;
      System.out.println("O valor total é: " + price);
    } else {
      System.out.println("Código inválido.");
    }
  }
}