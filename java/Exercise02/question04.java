import java.util.Scanner;

public class question04 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite o valor em graus Fahrenheit a ser convertido:\n");
		double fahrenheit = scanner.nextDouble();
		double celsius = (fahrenheit - 32) * 5 / 9;
		System.out.println("O valor em da temperatura convertido para Celsius é: " + celsius);

	}

}
