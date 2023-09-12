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
    @Override
    public String toString() {
        return String.format("%s/%s", num, denom);
    }
    public BigFraction add(BigFraction that){
        BigInteger top = num.multiply(that.denom).add(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    public BigFraction subtract(BigFraction that){
        BigInteger top = num.multiply(that.denom).subtract(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    public BigFraction multiply(BigFraction that){
        BigInteger top = num.multiply(that.num);
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
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
    public static BigFraction valueOf(long num, long denom){
        return new BigFraction(BigInteger.valueOf(num), BigInteger.valueOf(denom));
    }
}