import java.util.Scanner;

public class question06 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite um número inteiro:\n");
		int number = scanner.nextInt();

		if (number > 0) {
			int a = number;
			System.out.println("O número " + a + " é positivo.");
		} else {
			int b = number;
			System.out.println("O número " + b + " é negativo.");
		}

	}

}
