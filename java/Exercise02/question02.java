import java.util.Scanner;

public class question02 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		double dolarExchangeRate = 4.92;
		System.out.println("O valor do dólar no dia 04/05/2020 é: " + dolarExchangeRate);
		System.out.println("Digite o montante em dólares a ser convertido:\n");
		double dolarAmount = scanner.nextDouble();
		double value = dolarExchangeRate * dolarAmount;
		System.out.println("O valor da conversão em reais é: " + value);

	}

}
