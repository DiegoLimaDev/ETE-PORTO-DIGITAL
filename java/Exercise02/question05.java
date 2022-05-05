import java.util.Scanner;

public class question05 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite a primeira nota do aluno:\n");
		double n1 = scanner.nextDouble();
		System.out.println("Digite a segunda nota do aluno:\n");
		double n2 = scanner.nextDouble();
		System.out.println("Digite a terceira nota do aluno:\n");
		double n3 = scanner.nextDouble();
		System.out.println("Digite a quarta nota do aluno:\n");
		double n4 = scanner.nextDouble();
		double media = (n1 + n2 + n3 + n4) / 4;
		System.out.println("A média do aluno foi: " + media);

		if (media >= 7) {
			System.out.println("O aluno foi aprovado");
		} else {
			System.out.println("Digite a nota da recuperação:\n");
			double n5 = scanner.nextDouble();
			double mediaRecovery = (media + n5) / 2;
			System.out.println("A média da recuperação foi: " + mediaRecovery);

			if (mediaRecovery >= 7) {
				System.out.println("O aluno passou de ano.");
			} else {
				System.out.println("O aluno foi reprovado.");
			}

		}
	}

}
