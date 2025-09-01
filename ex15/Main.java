package ex15;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite tres números");
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		if (a > b && a > c) {
			System.out.println(a + " é o maior número");
		}
		else if (b > a && b > c) {
			System.out.println(b + " é o maior número");
		}
		else {
			System.out.println(c + " é o maior número");
		}
		sc.close();

	}

}
