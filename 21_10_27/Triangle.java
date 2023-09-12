import java.lang.Math;
public class Triangle {
    public double a;
    public double b;
    public double c;

    Triangle(double a, double b, double c){
        double h = radicand(a, b, c);
        if ( h < 0 ){
            throw new IllegalArgumentException();
        } else {
        this.a = a;
        this.b = b;
        this.c = c;
        }
    }
    public double area() {
        return radicand(a,b,c);
    }
    public double diameter(){
        return Math.max(a,Math.max(b,c));
    }
    public double perimeter(){
        return a+b+c;
    }
    public int numSides(){
        return 3;
    }
    private static double radicand(double a, double b, double c){
        double s = (a + b + c)/2.0;
        return s*(s-a)*(s-b)*(s-c);
    }
}
