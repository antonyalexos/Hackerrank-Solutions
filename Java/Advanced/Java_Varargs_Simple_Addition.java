import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

//Write your code here
class Add{
    
    public void add(int a1, int a2){
        System.out.println(a1+"+"+a2+"="+(a1+a2));
    }
    public void add(int a1, int a2, int a3){
        System.out.println(a1+"+"+a2+"+"+a3+"="+(a1+a2+a3));
    }
    public void add(int a1, int a2, int a3, int a4){
        System.out.println(a1+"+"+a2+"+"+a3+"+"+a4+"="+(a1+a2+a3+a4));
    }
    public void add(int a1, int a2, int a3, int a4, int a5){
        System.out.println(a1+"+"+a2+"+"+a3+"+"+a4+"+"+a5+"="+(a1+a2+a3+a4+a5));
    }
    public void add(int a1, int a2, int a3, int a4, int a5, int a6){
        System.out.println(a1+"+"+a2+"+"+a3+"+"+a4+"+"+a5+"+"+a6+"="+(a1+a2+a3+a4+a5+a6));
    }
}


public class Solution {
    
    public static void main(String[] args) {
        try{
            BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
            int n1=Integer.parseInt(br.readLine());
            int n2=Integer.parseInt(br.readLine());
            int n3=Integer.parseInt(br.readLine());
            int n4=Integer.parseInt(br.readLine());
            int n5=Integer.parseInt(br.readLine());
            int n6=Integer.parseInt(br.readLine());
            Add ob=new Add();
            ob.add(n1,n2);
            ob.add(n1,n2,n3);
            ob.add(n1,n2,n3,n4,n5);
            ob.add(n1,n2,n3,n4,n5,n6);
            Method[] methods=Add.class.getDeclaredMethods();
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
            e.printStackTrace();
        }
    }
}
