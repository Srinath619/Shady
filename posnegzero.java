import java.util.*;
 
class PosNegZero
{
    public static void main(String []s)
    {
        int n;

        Scanner sc=new Scanner(System.in);
         
        System.out.print("Enter any integer number: ");
        n=sc.nextInt();
         
      
        if(n>0)
            System.out.println(n + " is POSITIVE NUMBER.");
            
        else if(n<0)
            System.out.println(n + " is NEGATIVE NUMBER.");
            
        else
            System.out.println("IT's ZERO.");
         
    }
}
