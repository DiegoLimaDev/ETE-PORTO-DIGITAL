package questao2;

import java.util.Scanner;

public class main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println(
        "Esse algoritmo utiliza a informação de preço de determinado produto e quanto ele custaria sendo distribuído para as diferentes regiões do Brasil.");
    System.out.println("Digite o preço do produto em questão:");
    double price = scanner.nextDouble();
    System.out.println(
        "De acordo com os códigos a seguir selecione a região de distribuição:\n1 - Região norte: 5% de desconto\n2 - Região sul: 15% de desconto\n3 - Região sudeste: 7% de desconto\n4 - Região nordeste: 12% de desconto\n5 - Região centro-oeste: 20% de desconto.");
    int code = scanner.nextInt();
    if (code == 1) {
      price = price - (price * 0.05);
      System.out.println("O preço na região norte é: " + price);
    } else if (code == 2) {
      price = price - (price * 0.15);
      System.out.println("O preço na região sul é: " + price);
    } else if (code == 3) {
      price = price - (price * 0.07);
      System.out.println("O preço na região sudeste é: " + price);
    } else if (code == 4) {
      price = price - (price * 0.12);
      System.out.println("O preço na região nordeste é: " + price);
    } else if (code == 5) {
      price = price - (price * 0.20);
      System.out.println("O preço na região centro-oeste é: " + price);
    } else {
      System.out.println("O produto é importado.");
    }
  }

}
