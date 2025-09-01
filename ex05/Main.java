package ex05;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a, b, resultado;
		a = sc.nextInt();
		sc.nextLine();
		b = sc.nextInt();
		resultado = a + b;
		System.out.println("Entrada");
		System.out.println(a);
		System.out.println(b);
		System.out.println("Saída");
		System.out.println("Soma = " + resultado);
		
		
		sc.close();

	}

}
