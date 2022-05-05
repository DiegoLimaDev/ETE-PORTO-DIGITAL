import java.util.Scanner;

public class question08 {
  public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite um número inteiro:\n");
		double n1 = scanner.nextDouble();
		System.out.println("Digite um número inteiro:\n");
		double n2 = scanner.nextDouble();
		System.out.println("Escolha uma das opções a seguir:\n1 - Verificar se os números são pares\n2 - Verificar se a média dos números é maior que 7\n3 - Sair");
		int choice = scanner.nextInt();
		
		switch(choice) {
		case 1:
			if(n1 % 2 ==0 && n2 % 2 == 0){
			System.out.println("Os dois números são pares.");
			}else {
				System.out.println("Pelo menos um dos números é ímpar.");
			}
			break;
		case 2:
			if(((n1 + n2) / 2 )> 7) {
				System.out.println("A média é maior que 7.");
			}else {
				System.out.println("A média é menor que 7.");
			}
			break;
		case 3:
			System.out.println("Você escolheu sair do programa.");
		}
	}

}

}
