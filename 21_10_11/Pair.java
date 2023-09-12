public class Pair<S, T> {
    private S s;
    private T t; 
    public Pair(S s, T t){
        this.s = s;
        this.t = t;
    }
    public S getS(){
        return s;
    }
    public T getT(){
        return t;
    }
    @Override
    public String toString(){
        return  String.format("(%s, %s)", s.toString(), t.toString());
    } 
    public static void main (String[] args){
        Pair<String, String> quack = new Pair <>("duck", "l'orange");
        System.out.println(quack);
        Pair<String, Integer> ccEntry = new Pair<>("beep", 3);
        System.out.println(ccEntry);
    }
}