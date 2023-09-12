public class Square extends Rectangle {
    private double side;
    public Square(double side){
        super(side,side); // this MUST be the first line
        this.side = side;
    }
    @Override
    public String toString() {
        return String.format("Square(%s,%s)",side,side);
    }
}