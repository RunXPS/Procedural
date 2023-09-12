import java.math.BigInteger;
public class BigFraction {
    
    public static final BigFraction ZERO;
    public static final BigFraction ONE;
    public static final BigFraction HALF;
    static {
        ZERO = new BigFraction();
        ONE = BigFraction.valueOf(1, 1);
        HALF = BigFraction.valueOf(1, 2);
    }

    private final BigInteger num;
    private final BigInteger denom;

    public BigFraction(BigInteger num, BigInteger denom){
        if(denom.equals(BigInteger.ZERO)){
            throw new IllegalArgumentException();
        }
        if (denom.compareTo(BigInteger.ZERO) < 0){
            num = num.negate();
            denom = denom.negate();
        }
        BigInteger d = denom.gcd(num);
        num = num.divide(d);
        denom = denom.divide(d);
        this.num = num;
        this.denom = denom;
    }
    /**
     * This creates the big fraction 0/1
     */
    public BigFraction(){
        this(BigInteger.ZERO, BigInteger.ONE);
    }
    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof BigFraction)){
            return false;
        }
        BigFraction that = (BigFraction)obj;
        return num.equals(that.num) && denom.equals(that.denom);
    }
    /**
     * Creates a string representation of the form numerator/denominator
     * @return numerator/denominator in a string
     */
    @Override
    public String toString() {
        return String.format("%s/%s", num, denom);
    }
    /**
     * This calculates this + that
     * @param that the Big Fraction we are adding to this Big Fraction
     * @return this + that
     */
    public BigFraction add(BigFraction that){
        BigInteger top = num.multiply(that.denom).add(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    /**
     * This calculates this - that
     * @param that the Big Fraction we are subtracting from this Big Fraction
     * @return this - that
     */
    public BigFraction subtract(BigFraction that){
        BigInteger top = num.multiply(that.denom).subtract(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    /**
     * This calculates this * that
     * @param that the Big Fraction we are multiplying this Big Fraction
     * @return this * that
     */
    public BigFraction multiply(BigFraction that){
        BigInteger top = num.multiply(that.num);
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    /**
     * This calculates this / that
     * @param that the Big Fraction we are dividing this Big Fraction
     * @return this / that
     */
    public BigFraction divide(BigFraction that){
        BigInteger top = num.multiply(that.denom);
        BigInteger bottom = denom.multiply(that.num);
        return new BigFraction(top, bottom);
    }
    public static void main(String[] args) {
        BigFraction bf = valueOf(3,4);
        System.out.println(bf);
        BigFraction bf2 = valueOf(-6,-8);
        System.out.println(bf2);
        BigFraction bf3 = valueOf(1,3);
        BigFraction bf4 = valueOf(1, 2);
        System.out.println(bf.equals(bf2));
        System.out.println(bf3.add(bf4));
        BigFraction total = new BigFraction();
        for (int k = 0; k <= 1000; k++){
            total = total.add(BigFraction.valueOf(1, k));
        }
        System.out.println(total);
    }
    /**
     * This static factory method allows a BigFraction to be specified
     * with two <code>long</code>s.
     * @param num the numerator we are using
     * @param denom the denominator we are using
     * @return  BigFraction num/denom 
     */
    public static BigFraction valueOf(long num, long denom){
        return new BigFraction(BigInteger.valueOf(num), BigInteger.valueOf(denom));
    }
}