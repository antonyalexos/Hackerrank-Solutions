import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        BigInteger a = scan.nextBigInteger();
        BigInteger b = scan.nextBigInteger();
        BigInteger sum = a.add(b);
        BigInteger mult = a.multiply(b);
        
        System.out.println(sum);
        System.out.println(mult);
    }
}
