package questao5;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Qual o nome do funcionário?");
    String name = scanner.next();
    System.out.println("O funcionário e do gênero:\n1 - Masculino\n2 - Feminino");
    int gender = scanner.nextInt();
    System.out.println("Qual a idade do funcionário?");
    int age = scanner.nextInt();
    System.out.println("Qual o salário do funcionário?");
    double paycheck = scanner.nextDouble();
    if (gender == 1 && age >= 30) {
      paycheck = paycheck + 100;
      System.out.println("O salário líquido do funcionário " + name + " é " + paycheck);
    } else if (gender == 1 && age < 30) {
      paycheck = paycheck + 50;
      System.out.println("O salário líquido do funcionário " + name + " é " + paycheck);
    } else if (gender == 2 && age >= 30) {
      paycheck = paycheck + 200;
      System.out.println("O salário líquido do funcionário " + name + " é " + paycheck);
    } else if (gender == 2 && age < 30) {
      paycheck = paycheck + 80;
      System.out.println("O salário líquido do funcionário " + name + " é " + paycheck);
    } else {
      System.out.println("Algum dado digitado foi inválido.");
    }

  }

}
