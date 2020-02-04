import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

import static java.lang.System.in;

class Prime{
    public void checkPrime(int... integers){
        boolean flag = true;
        for(int i:integers){
            if(i<2) flag = false;
            for(int j=2;j<i;j++){
                if(i%j==0){
                    flag = false;
                    break;
                }
            }
            if(flag) System.out.print(i+ " ");
            flag = true;
        }
        System.out.println();
    }
}
//import static java.lang.System.*;
//
//class Prime {
//
//    void checkPrime(int... numbers) {
//
//        for (int number : numbers) {
//            if (BigInteger.valueOf(number).isProbablePrime(1)) {
//                System.out.print(number + " ");
//            }
//        }
//
//        System.out.println();
//    }
//}




public class Solution {
    
    public static void main(String[] args) {
        try{
            BufferedReader br=new BufferedReader(new InputStreamReader(in));
            int n1=Integer.parseInt(br.readLine());
            int n2=Integer.parseInt(br.readLine());
            int n3=Integer.parseInt(br.readLine());
            int n4=Integer.parseInt(br.readLine());
            int n5=Integer.parseInt(br.readLine());
            Prime ob=new Prime();
            ob.checkPrime(n1);
            ob.checkPrime(n1,n2);
            ob.checkPrime(n1,n2,n3);
            ob.checkPrime(n1,n2,n3,n4,n5);
            Method[] methods=Prime.class.getDeclaredMethods();
            Set<String> set=new HashSet<>();
            boolean overload=false;
            for(int i=0;i<methods.length;i++)
            {
                if(set.contains(methods[i].getName()))
                {
                    overload=true;
                    break;
                }
                set.add(methods[i].getName());
                
            }
            if(overload)
            {
                throw new Exception("Overloading not allowed");
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
    
}
