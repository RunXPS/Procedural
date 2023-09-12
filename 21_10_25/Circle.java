public class Circle implements Shape {
    private double radius;
    public Circle(double radius){
        this.radius = radius;
    }
    public double area(){
        return Math.PI*radius*radius;
    }
    public double diameter(){
        return 2*radius;
    }
    public double perimeter(){
        return 2*Math.PI*radius;
    }
    @Override
    public String toString(){
        return String.format("Circle(%s)",radius);
    }
}