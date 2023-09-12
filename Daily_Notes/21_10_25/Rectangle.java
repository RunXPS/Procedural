public class Rectangle implements Polygon{
    public double width;
    public double length;
    public Rectangle(double width, double length){
        this.width = width;
        this.length = length;
    }
    public double area(){
        return width*length;
    }
    public double diameter(){
        return Math.hypot(width, length);
    }
    public double perimeter(){
        return 2*(width*length);

    }
    public int numSides(){
        return 4;
    }
    @Override
    public String toString() {
        return String.format("Rectangle(%s,%s)", length, width);
    }
}