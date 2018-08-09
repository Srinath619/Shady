package GuviPlayerSet4;

import java.util.Scanner;

public class WaysToFormAnumberUsing1and2 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int a=in.nextInt();
        int ways=a/2+1;
        System.out.println(ways);
       }
}
