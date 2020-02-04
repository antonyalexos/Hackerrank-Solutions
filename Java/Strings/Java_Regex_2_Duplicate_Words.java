//code's not mine

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DuplicateWords {
    
    public static void main(String[] args) {
        
        String regex = "\\b(\\w+)(\\b\\W+\\b\\1\\b)*";
        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        
        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());
        
        while (numSentences-- > 0) {
            String input = in.nextLine();
            
            Matcher m = p.matcher(input);
            // Check for subsequences of input that match the compiled pattern
            while (m.find()) {
                input = input.replaceAll(m.group(0),m.group(1));
            }
            
            // Prints the modified sentence.
            System.out.println(input);
        }
        
        in.close();
    }
}

//\w ----> A word character: [a-zA-Z_0-9]
//\W ----> A non-word character: [^\w]
//\b ----> A word boundary
//\1 ----> Matches whatever was matched in the 1st group of parentheses, which in this case is the (\w+)
//The \b boundaries are needed for special cases such as "Bob and Andy" (we don't want to match "and" twice). Another special case is "My thesis is great" (we don't want to match "is" twice).

