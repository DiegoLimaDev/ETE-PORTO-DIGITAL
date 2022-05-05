import java.util.Scanner;

public class question03 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite o valor em graus Celsius a ser convertido:\n");
		double celsius = scanner.nextDouble();
		double fahrenheit = (9 * celsius + 160) / 5;
		System.out.println("O valor em da temperatura convertido para fahrenheit é: " + fahrenheit);

	}

}
