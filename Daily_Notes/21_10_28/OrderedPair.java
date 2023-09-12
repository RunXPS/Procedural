import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class OrderedPair implements Comparable<OrderedPair> {
    
    private int x;
    private int y;
    public OrderedPair(int x, int y){
        this.x = x;
        this.y = y;
    }
    public int compareTo (OrderedPair that){
        if (x == that.x){
            return y - that.y;
        }
        return x - that.x;
    }
    @Override
    public String toString(){
        return String.format("(%s, %s)", x, y);
    }
    public static void main(String[] args) {
        ArrayList<OrderedPair> pairs = new ArrayList<>();
        pairs.add(new OrderedPair(1,2));
        pairs.add(new OrderedPair(1,3));
        pairs.add(new OrderedPair(2,2));
        pairs.add(new OrderedPair(3,4));
        pairs.add(new OrderedPair(3,0));
        System.out.println("Before:\t\t" + pairs);
        Comparator<OrderedPair> byFirst = (a, b) -> 
        {
            if (a.x == b.x){
                return a.y - b.y;
            }
            return a.x - b.x;
        };
        Collections.sort(pairs,byFirst);
        System.out.println("byFirst:\t" + pairs);
        Comparator<OrderedPair> bySum = (a,b) ->
        {
            return (a.x + a.y) - (b.x + b.y);   
        };
        Collections.sort(pairs,bySum);
        System.out.println("bySum:\t\t" + pairs);
        Collections.sort(pairs);
        System.out.println("compareTo:\t" + pairs);
    }
}