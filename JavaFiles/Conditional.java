import java.lang.Math;
public class Conditional
{
    /**
     * This computes the positive part of a number
     * @param x the number we are computing the positive  part of
     * @return x if x > 0 and 0 otherwise.
     */
    public static double positivePart(double x)
    {   
        if (x > 0){
            return x;
        }
        return 0;
    }
    /**
     * This computes the negative part of a number
     * @param x the number we are computing the negative  part of
     * @return -x if x < 0 and 0 otherwise.
     */
    public static double negativePart(double x)
    {
        if (x < 0){
            return -x;
        }
        return 0;
    }
    /**
     * Use this to check sufficient closeness of floating-point numbers
     */
    public static boolean closeEnough(double x, double y)
    {
        return Math.abs(x - y) < 1e-6;
    }
    /**
     * This implements a stepwise defined function
     * @param x the argument of this function
     * @return 4 - x*x if x < -2, 0 if |x| <= 2 and x - 2 otherwise
     */
    public static double mathCheese(double x)
    {
        return x < -2? 4 - x*x : Math.abs(x) <= 2? 0 : x-2; 
    }
    /**
     * This checks if an alphabetical string is in the
     * first half of the alphabeet.
     * @param s the String to be checked; this string must contain
     * only alphabetical characters and this check is case-insensitive
     * @return true if the s starts with a-m and false otherwise.
     */
    public static boolean isInFirstHalfOfAlphabet(String s)
    {
        s = s.toLowerCase();
        return s.codePointAt(0) <= 109 && s.codePointAt(0) >= 97? true : false;
    }
    /**
     * This assigns a letter grade on a ten-point scale
     * @param score a final average of grades
     * @return "A" if the score is 90 or above, "B" if the score is 
     * 80 or above, etc.  IF the score is under 60, return "F"
     */
    public static String assignLetterGrade(int score)
    {
        return score >= 90? "A" : score >= 80? "B" : score >= 70? "C" : score >= 60? "D" : "F";
    }
    /**
     * This implements +/- grading.  The grade of F gets no +- modifier.
     * @return "+" if the second digit of the grade is 8 or higher,
     * a "-" if the second digit of the grade is 2 or lower, and
     * a "" otherwise.  Special note: any score of 98 or higher is an A+;
     * an average can exceed 100.
     */
    public static String assignPlusMinus(int score)
    {
        int ones = score%10;
        String grade = assignLetterGrade(score);
        return score >= 98? "+A" : grade == "F"? grade : ones >= 8? "+" + grade : ones <= 2? "-" + grade : grade;
    }
    /**
     * This assigns the full grade
     * @param score the final average
     * @return a +- grade for the average
     */
    public static String assignGrade(int score)
    {
        return assignPlusMinus(score);
    }
    public static void main(String[] args)
    {
        //test your functions in here.  Example
        System.out.println("Testing positivePart:");
        double x = 5;
        System.out.printf("Case x = %s: %s\n",  x,  closeEnough(5, positivePart(x)));
        x = 0;
        System.out.printf("Case x = %s: %s\n",  x,  closeEnough(0, positivePart(x)));
        x = -5;
        System.out.printf("Case x = %s: %s\n",  x,  closeEnough(0, positivePart(x)));
        System.out.println("Testing negativePart:");
        System.out.println("is 0: " + negativePart(5));
        System.out.println("is 0: " + negativePart(0));
        System.out.println("is 5: " + negativePart(-5));
        System.out.println("Testing mathCheese:");
        System.out.println("is 3: " + mathCheese(5));
        System.out.println("is 0: " + mathCheese(0));
        System.out.println("is -21: " + mathCheese(-5));
        System.out.println("Testing isInFirstHalfOfAlphabet:");
        System.out.println("Andy == true: " + isInFirstHalfOfAlphabet("Andy"));
        System.out.println("Zurg == false: " + isInFirstHalfOfAlphabet("Zurg"));
        String test = "naiman";
        System.out.printf("Case x = %s: %s\n", test , !isInFirstHalfOfAlphabet(test)); 
        System.out.println("Testing assignGrade:");
        System.out.println("90 == -A: " + assignGrade(90));
        System.out.println("65 == D: " + assignGrade(65));
        System.out.println("56 == F: " + assignGrade(56));
        System.out.println("100 == +A: " + assignGrade(100));
    }
}