import java.io.*;
import java.util.*;
public class Solution {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if(!scan.hasNext()) {
            System.out.print("0");
            return;
        }
        String s = scan.nextLine();
        if (s == null || s.equals("") || s.trim().equals("")){
            System.out.println("0");
        }
        // Write your code here.
        String[] parts = s.trim().split("[\\p{Punct}\\s]+");
        System.out.println(parts.length);
        for(int i=0;i<parts.length;i++){
            System.out.println(parts[i]);
        }
        scan.close();
    }
}
