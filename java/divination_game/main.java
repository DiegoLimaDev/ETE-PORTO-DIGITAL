import java.util.Scanner;
import java.util.Random;

public class main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();
    int randomize = random.nextInt(100) + 1;
    System.out.println(
        "Esse código gera um número aleatório de 0 à 100 e você tem 10 chances para adivinhar qual número gerado.");

    int i;
    for (i = 0; i < 10; i++) {
      System.out.println("Digite seu palpite para o número gerado:");
      int guess = scanner.nextInt();
      if (guess == randomize) {
        System.out.println("Parabéns você acertou o número.\n");
        break;
      } else if (i == 9) {
        System.out.println("Suas tentativas acabaram. Você perdeu.");
      } else {
        if (guess > randomize) {
          System.out.println("Você não acertou. Seu palpite foi maior que o número gerado.\n");
        } else {
          System.out.println("Você não acertou. Seu palpite foi menor que o número gerado.\n");
        }
      }
    }
  }
}