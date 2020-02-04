import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        try{
            Scanner scan = new Scanner(System.in);
            int a = scan.nextInt();
            int b = scan.nextInt();
            System.out.println(a/b);
        }
        catch(InputMismatchException ex){System.out.println("java.util.InputMismatchException");}
        catch(ArithmeticException ex){System.out.println("java.lang.ArithmeticException: / by zero");}
    }
}
