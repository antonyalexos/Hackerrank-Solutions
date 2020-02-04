import java.math.BigDecimal;
import java.util.*;
class Solution{
    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();
        
        Arrays.sort(s, 0, n, (num1, num2) -> {
            BigDecimal a = new BigDecimal(num1);
            BigDecimal b = new BigDecimal(num2);
            return b.compareTo(a);
        });
        
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}
