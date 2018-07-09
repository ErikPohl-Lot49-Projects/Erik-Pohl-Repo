public class UseCaseApp {
	public static void main(String[] args) {
		for (int i=0;i<=12;i++) {
			System.out.printf("Fibonacci number for sequence [%d] is [%d]%n",i,UseCase.fibonacci(i));
		}
	}
}
