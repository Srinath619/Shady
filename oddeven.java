import java.util.Scanner;

public class oddeven
{
    public static void main(String args[])
    {
        int a;
        Scanner scan = new Scanner(System.in);
		
        System.out.print("Enter a Number : ");
        a = scan.nextInt();
		
        if(a%2 == 0)
        {
            System.out.print("It is an Even Number");
        }
        else
        {
            System.out.print("It is an Odd Number");
        }
    }
}
