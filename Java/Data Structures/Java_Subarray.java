import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int sum = 0, counter = 0;
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int []a = new int[n];
        for(int i =0;i<n;i++){
            a[i] = scan.nextInt();
        }
        for(int j=0;j<n;j++){
            for(int k=0;k<n;k++){
                if((k+j)>=n) continue;
                sum = sum + a[k+j];
                if(sum<0) counter++;
            }
            sum = 0;
        }
        System.out.println(counter);
    }
}
