/*
 * This is a class of 3D immutible vectors with
 * integer coefficients.
 */
public class Vector3D implements IVector3D
{
    //initialize in a static block
    /**
     * This is the magnitude and directon on the x coordinate
     */
    public static final Vector3D I;
    /**
     * This is the magnitude and directon on the y coordinate
     */
    public static final Vector3D J;
    /**
     * This is the magnitude and directon on the z coordinate
     */
    public static final Vector3D K;
    /**
     * This is the default value of a vector at 0x,0y,0z
     */
    public static final Vector3D ZERO;
    /*
     * @param a coefficient of I
     * @param b coefficient of J
     * @param c coefficient of K
     * This makes ai + bj + ck
     */
    static {
        I = new Vector3D(1,0,0);
        J = new Vector3D(0,1,0);
        K = new Vector3D(0,0,1);
        ZERO = new Vector3D();
    }
    private int a;
    private int b;
    private int c;
    /** 
     * This initializes a new Vector3D
     * @param a the magnitude of the x direction
     * @param b the magnitude of the y direction
     * @param c the magnitude of the z direction
    */
    public Vector3D(int a, int b, int c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    /**
     * This makes the zero vector
     */
    public Vector3D()
    {
        this(0,0,0);
    }
    /**
     * @param that another IVector3D
     * @return  the dot product of this vector and that.
     */
    public int dot(Vector3D that)
    {
        return this.a*that.a + this.b*that.b + this.c*that.c;
    }
    /**
     * @param that anohter IVector3D
     * @return  the cross product of this vector and that.
     */
    public Vector3D cross(Vector3D that)
    {
        return new Vector3D(this.b*that.c - this.c*that.b, -(this.a*that.c - c*that.a), this.a*that.b - this.b*that.a);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return  the that*this
     */
    public Vector3D scalarMultiply(int scalar)
    {        
        return new Vector3D(scalar*a, scalar*b, scalar*c);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this + that
     */
    public Vector3D add(Vector3D that)
    {
        return new Vector3D(a + that.a, b + that.b, c + that.c);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this - that
     */
    public Vector3D subtract(Vector3D that)
    {
        return new Vector3D(a - that.a, b - that.b, c - that.c);
    }
    /**
     * @return the length of this vector
     */
    public double magnitude()
    {
        return a+b+c;
    }
    /**
     * @param that another vector
     * @return the angle between this and that in radians in [0,π]
     */
    public double angleBetween(Vector3D that)
    {
        double x = this.dot(that);
        if (x == 0){
            return Math.PI/2;
        }
        x /= magnitude();
        x /= that.magnitude();
        return Math.acos(x);
    }
    /**
     * @return A string representation of the form ai + bj + ck.
     * Make sure you have negative terms not looking like crap.
     */
    @Override 
    public String toString()
    {
        return String.format("(%s,%s,%s)", a, b, c);
    }
    @Override 
    public boolean equals(Object o)
    {
        if (!(o instanceof Vector3D)){
            return false;
        }
        Vector3D that = (Vector3D)o;
        return a == that.a && b == that.b && c == that.c;
    }
    public static void main(String[] args) {
        Vector3D zero = new Vector3D();
        System.out.println("Zero : " + zero);
        Vector3D vector1 = new Vector3D(1,2,3);
        Vector3D vector05 = new Vector3D(4,-5,6);
        System.out.println("dot product = 12: " + vector1.dot(vector05));
        Vector3D vector2 = new Vector3D(4,5,6);
        Vector3D vector3 = new Vector3D(3,-3,1);
        Vector3D vector4 = new Vector3D(4,9,2);
        System.out.println("dot product = (-15,-2,39): " + vector3.cross(vector4));
        System.out.println("scalar multiply (2,4,6): " + vector1.scalarMultiply(2));
        System.out.println("Vector add (5,7,9): " + vector1.add(vector2));
        System.out.println("Vector add (3,3,3): " + vector2.subtract(vector1));
        System.out.println("angle between: " + vector1.angleBetween(vector2));
        System.out.println("Vector 1 == 2: " + vector1.equals(vector2));
    }
}