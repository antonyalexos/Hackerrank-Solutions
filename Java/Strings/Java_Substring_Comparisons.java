import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < s.length(); i++) {
            if (s.length() - i >= k) {
                list.add(s.substring(i, k + i));
            }
        }
        Collections.sort(list);
        smallest = list.get(0);
        largest = list.get(list.size() - 1);
        
        return smallest + "\n" + largest;
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
        
        System.out.println(getSmallestAndLargest(s, k));
    }
}
