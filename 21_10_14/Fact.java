import java.math.BigInteger;
public class Fact{
    public static BigInteger factorial(int n){
        if (n < 0){
            throw new IllegalArgumentException();
        }
        if (n == 1 || n == 0) {
            return BigInteger.ONE;
        }
        return BigInteger.valueOf(n).multiply(factorial(n-1));
    }
///... = stargument
//stargument must be last arguement
//no keyword arguements in java
//but you fo have method name overloading
public static int wabbit(int...factors){
    int out = 1;
    for (int f: factors){
        out *= f;
    }
    return out;
}
public static void main(String[] args){
    System.out.println(factorial(1000));
    System.out.println(factorial(3));
    //System.out.println(factorial(-3));
    System.out.println(wabbit(2,3,4,5,6));
}
}