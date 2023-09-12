import java.util.ArrayList;
import java.math.BigInteger;
public class Loopy
{
    public static void main(String[] args)
    {
        System.out.println("tableOfSquares: ");
        System.out.println(tableOfSquares(1, 5, 1));
        System.out.println("firstHalf: ");
        ArrayList<String> emails = new ArrayList<>();
        emails.add("Barry");
        emails.add("Zeke");
        emails.add("Kyle");
        emails.add("Andy");
        emails.add("Tony");
        emails.add("Charlie");
        System.out.println("\t " + firstHalf(emails));
        System.out.print("firstHalfInPlace: \n\t ");
        firstHalfInPlace(emails);
        System.out.println("purmutations: ");
        System.out.println("\t 6 : " + permutations(3, 3));
        System.out.println("choose: ");
        System.out.println("\t 1 : " + choose(3,3));
    }
    /**
     * produce a table of values for the square function starting
     * at start, ending before end, and which increments the x-value
     * by increment. Return this in a string.
     */
    public static String tableOfSquares(double start, double end, double increment)
    {
        ArrayList<Double> coreNumber = new ArrayList <>();
        ArrayList<Double> square = new ArrayList<>();
        String out = "root\t\t|\t\tsquare\n";
        while (start < end){
            coreNumber.add(start);
            square.add(Math.pow(start,2.0));
            start += increment;
        }
        for (int i = 0; i < square.size(); i++){
            out += coreNumber.get(i).toString() + "\t\t|\t\t" + square.get(i).toString() + "\n";
        }
        return out;
    }
    /**
     * @param roster a list of email names
     * @return an ArrayList of names in the first half of the alphabet, case insensitive
     */
    public static ArrayList<String> firstHalf(ArrayList<String> roster)
    {
        ArrayList<String> out = new ArrayList <>(); 
        for (String email : roster){
            if (email.toLowerCase().codePointAt(0) >= 97 && email.toLowerCase().codePointAt(0) <= 109){
                out.add(email);
            }
        }
        return out;
    }
    /**
     * @param roster a list of email names
     * This has the side-effect of filtering in all elements in the
     * first half of the alphabet, case insensitive.
     */
    public static void firstHalfInPlace(ArrayList<String> roster)
    {
        ArrayList<String> excluded = firstHalf(roster);
        boolean arranged = false;

        //for (String email : excluded){
        while (arranged == false) {
            boolean complete = true;
            for (int i = 0; i < excluded.size()-1; i++) {
                if ((excluded.get(i)).codePointAt(0) > (excluded.get(i+1)).codePointAt(0)){
                    String temp = excluded.get(i);
                    excluded.set(i,excluded.get(i+1));
                    excluded.set(i+1, temp);
                    complete = false;
                }
            }
            if (complete == true){
                arranged = true;
            }
        }
        System.out.println(excluded);
    }
    /**
     * @param n the size of the population
     * @param k the size of the sample
     * @return the number of ordered samples of size k 
     * in the population. This is n(n-1)(n-2).....  (n-k+1).
     */
    public static BigInteger permutations(int n, int k)
    {
        BigInteger out = new BigInteger( Integer.toString(n) );
        for (int i = 1; i < k; i++){
            BigInteger temp = new BigInteger( Integer.toString(n-i) );
            out = out.multiply(temp);
        }
        return out;
    }
    /**
     * @param n the size of the population
     * @param k the size of the sample
     * @return the number of ordered samples of size k 
     * in the population. This is 
     * n(n-1)(n-2).....  (n-k+1)/k!.
     * Be smart:  the product  of any k consecutive integers
     * is divisible by k.  You should be able to compute
     * choose(1000000000, 3).  hint: ZIPPER
     */
    //10  9  8  7  6
    // | /| /| /| /|
    //1   2  3  4  5
    //mult down, then across
    public static BigInteger choose(int n, int k)
    {
        BigInteger x = permutations(n,k);
        BigInteger factorial = new BigInteger(Integer.toString(k));
        for (int i = 1; i < k; i++){
            BigInteger temp = new BigInteger( Integer.toString(i) );
            factorial = factorial.multiply(temp);
        }
        x = x.divide(factorial);
        return x;
    }
}