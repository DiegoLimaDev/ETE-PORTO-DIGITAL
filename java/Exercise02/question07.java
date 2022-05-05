import java.util.Scanner;

public class question07 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out
				.println("Escolha uma das operações abaixo:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n");
		int operacao = scanner.nextInt();
		System.out.println("Digite o primeiro número da operação:\n");
		int n1 = scanner.nextInt();
		System.out.println("Digite o segundo número da operação:\n");
		int n2 = scanner.nextInt();

		switch (operacao) {
			case 1:
				System.out.println("O valor da soma é: " + (n1 + n2));
				break;
			case 2:
				System.out.println("O valor da subtração é: " + (n1 - n2));
				break;
			case 3:
				System.out.println("O valor da multiplicação é: " + (n1 * n2));
				break;
			case 4:
				System.out.println("O valor da divisão é: " + (n1 + n2));
				break;
		}

	}

}
