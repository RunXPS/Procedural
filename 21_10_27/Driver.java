public class Driver {
    public static void main(String[] args) {
        Polygon s = new Square(10);
        System.out.println("area: " + s.area());
        System.out.println("diameter: " + s.diameter());
        System.out.println("perimeter: " + s.perimeter());
        System.out.println("sides: " + s.sides());
    }
}
