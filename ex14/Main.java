package ex14;
import java.util.Locale;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite a temperatura em celcius:");
		double c = sc.nextDouble();
		double f = 9 * c / 5 + 32;
		System.out.printf("Equivalente em Fahrenheit : %.1f%n", f);
		System.out.print("Deseja repetir (s/n)?");
		char resp = sc.next().toLowerCase().charAt(0);
		while (resp != 'n') {
			System.out.println("Digite a temperatura em celcius:");
			c = sc.nextDouble();
			f = 9 * c / 5 + 32;
			System.out.printf("Equivalente em Fahrenheit : %.1f%n", f);
			System.out.print("Deseja repetir (s/n)?");
			resp = sc.next().toLowerCase().charAt(0);
		}
		
		
		
		
		
		sc.close();
		

	}

}
