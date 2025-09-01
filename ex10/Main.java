package ex10;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1;
		System.out.println("Digite um número");
		 n1 = sc.nextInt();
		 if (n1 % 2 == 0) {
			 System.out.println("Par");
		 }
		 else {
			 System.out.println("Impar");
		 }
		
		sc.close();

	}

}
