package ex09;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1;
		System.out.println("Digite um número");
		n1 = sc.nextInt();
		if (n1 <0) {
			System.out.println("Esse número é negativo");
		}
		else {
			System.out.println("Esse número é positivo");
		}
		
		
		sc.close();

	}

}
