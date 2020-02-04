import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int sum = 0;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            for(int j=1;j<=n;j++){
                sum = a;
                for(int k=0;k<j;k++){
                    sum = sum + (int)(b*Math.pow(2,k));
                }
                System.out.print(sum+" ");
            }
            sum = 0;
            System.out.println();
        }
        
        in.close();
    }
}
