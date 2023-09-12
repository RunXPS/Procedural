import java.util.ArrayList;
import java.util.Arrays;
import java.math.BigInteger;
import java.time.LocalDate;
/**
*  Glorious Lab Practical on Java
*/
public class LP1
{
    /** 
     * This computes  the sum of a list of BigIntegers
     * @param a an array list of BigIntegers
     * @return the sum of the BigIntegers in a
     */
    public static BigInteger sum(ArrayList<BigInteger> a)
    {   
        BigInteger out = BigInteger.ZERO;
        for (int i = 0; i < a.size(); i++){
            out.add(a.get(i));
        }
        return out;
    }   
	/**
	* This plucks out entries of a string at indices divisible by p.
    * in a string.  
    * @param s a string
    * @param p a nonnegative integer.  
    * @return a string that has entries p, 2p, 3p,   etc of the
    * string s.
    *  Examples:
    * aerate("aardwolf" 2) -&gt; "arwl"
    * aerate("bacchanalia" 3) -&gt; "bcni"
    */    
	public static String aerate(String s, int p)
	{
        String out = "";
        int count = 0;
        while (count < s.length()){
        out += s.charAt(count);
        count += p;
        }
        return out;
	}
    /**
     * This makes a string echoy.  See the example
     * @param s is a string
     * @return a string with the nth character repeated n times.  
     * example:  echoy("cowpie") &rarr; coowwwppppiiiiieeeeee
     * if the string passed is empty, return an empty string
     */
    public static String echoy(String s)
    {
        return "";
    }
    /** 
     * This computes the product of the non-zero elements of
     * a and returns the sum of its digits.
     * @param a an array list
     * @return the sum of the digits in the product of the 
     * non-zero entries in a
     */
    public static int  finger(ArrayList<BigInteger>  a)  
    {   
        return 0;
    }   
    /**
     * This filters strings for a specified substring
     * @param al is an array list of strings.
     * @param s is a search string
     * @return an array list of striings containing all those strings
     * in the array list <code>al</code> having <code>s</code> as a substring.
     */
     public static ArrayList<String> pseudoGrep(ArrayList<String> al, String s)
     {
         return new ArrayList<String>();
     }
    /**
    *  This finds the date n days from today.  If n is negative
    *  find the date -n days ago.
    *  @param n the number of days from today
    *  @return the date n days from today.  
    *  Sample:  10000 days from this lab prac is 29 March 2049.
    *  Today is 11 November 2021
    *  Sample:  10000 days ago is 1994-06-26
    */
    public static LocalDate daysFromNow(int n)
    {
        return LocalDate.EPOCH;
    }
    /** 
    *  Here is your testing ground.
    *  @param args command-line arguments. You won't have any.
    */
    public static void main(String[] args)
    {
        ArrayList<BigInteger> nums = new ArrayList<>();
        nums.add(BigInteger.ONE);
        nums.add(BigInteger.TEN);
        nums.add(BigInteger.TWO);
        System.out.println(sum(nums).toString());
        //System.out.println(daysFromNow(0));        
    }
}