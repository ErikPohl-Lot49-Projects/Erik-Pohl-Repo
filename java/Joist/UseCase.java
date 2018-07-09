
public class UseCase {

	public static int fibonacci(int n)
    {
		if (n < 1) {return 0;}
        if (n==1) {return 1;}
        if (n==2) {return 1;}
        return add(fibonacci(n-1), fibonacci(n-2));    
    }
	
	public static int add(int a, int b)
	{
		return a+b;
	}
	
}
