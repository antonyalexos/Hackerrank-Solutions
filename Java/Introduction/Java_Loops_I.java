import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        for(int i = 1; i <= 10;i++){
            System.out.println(x+" x "+i+" = "+x*i);
        }
        
    }
}
