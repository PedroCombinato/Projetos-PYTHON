package ex06;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a,area;
		int b;
		a = 3.14159;
		b = sc.nextInt();
		area = a * Math.pow(b,2);
		System.out.println("Área =" + area);
		
		sc.close();
	}

}
