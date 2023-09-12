public class point {
    private final int x;
    private final int y; //final means "cannot be reassigned"

    public point(int x,int y){
        this.x = x;
        this.y = y;
    }
    /* 
     * method name overloading
     * several methods can have the same name if their
     * sigs are different
     * 
     * You should only use this for closeley relared methods
     */
    public point(){ //sig is []
        //x = 0;
        //y = 0;
        this(0,0); //calls sibling constructor
    }
    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }
    
    @Override
    public String toString(){
        return String.format("%s,%s", x, y);
    }
    @Override
    public boolean equals(Object o){
        if(this == o){
            return true;
        }
        if(!(o instanceof point)){
            return false;
        }
        //o must be a point
        point that = (point) o;
        return x == that.x && that.y == y;
    }

    public double distanceTo(point other){
        return Math.hypot(x-other.x, y - other.y);
    }
    
    public point reflectAcrossX(){
        return new point(x, -y);
    }public point reflectAcrossY(){
        return new point(-x, y);
    }
    public point reflectAcrossXequalsY(){
        return new point(x, y);
    }
    
    public static void main(String[] args){
        point p = new point(3,4);
        point q = new point(0,0);
        point s = new point(3,4);
        System.out.print("P == S: ");
        System.out.println(p == s);
        //System.out.println(p.x);
        //System.out.println(p.y);
        System.out.print("Distance to points: ");
        System.out.println(p.distanceTo(q));
        //System.out.println(p);
        System.out.print("Reflect across X: ");
        System.out.println(p.reflectAcrossX());
    }
}