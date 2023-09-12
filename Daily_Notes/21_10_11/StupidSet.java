import java.util.ArrayList;
public class StupidSet<T>
{
    private ArrayList<T> elements;
    private int size;
    /**
     * @param items is an array list of items to
     * put in our StupidSet without duplicates
     */
    public StupidSet(ArrayList<T> items)
    {
        this.elements = new ArrayList <>();
        for (T item:items){
            if (!elements.contains(item)){
                elements.add(item);
                size++;
            }
        }
    }
    /**
     * This makes an empty StupidSet
     */
    public StupidSet()
    {
        this(new ArrayList <>());
    }
    /**
     * This adds a new item to our StupidSet and returns
     * <code>false</code> if the item is already present.
     * @param newItem the new item we are adding
     * @return false if the new item is not added and
     * <code>true</code> otherwise.
     */
    public boolean add(T newItem)
    {
            if (elements.contains(newItem)) { 
                return false;
            }
        elements.add(newItem);
        return true;
    }    
    /**
     * This checks for the presence of <code> item</code>
     * in this StupidSet.
     * @param item the new item we are checking for
     * @return false if the item is not present
     * <code>true</code> otherwise.
     */
    public boolean contains(T newItem)
    {
        return elements.contains(newItem);
    }    
    /**
     * This checks to see if <code>other</code> is
     * a subset of this StupidSet.
     * @param item a Stupidset
     * @return <code>true</code> if every element of 
     * <code>other</code> belongs to this StupidSet
     * and <code>false</code> otherwise.
     */
    public boolean containsAll(StupidSet<T> other)
    {
        for (int i = 0; i < other.elements.size(); i++){
            if (!(elements.contains(other.elements.get(i)))){
                return false;
            }
        }
        return true;
    }    
    /**
     * This removes <code>item</code> if it is present
     * @param item the item we are trying to remove
     * @return false if the item is not present
     * <code>true</code> if the item got removed.
     */
    public boolean remove(T item)
    {
        for (int i = 0; i < size; i++){
            if (elements.get(i) == item){
                elements.remove(i);
                return true;
            }
        }
        return false;
    }    
    /**
     * This adds all items in moreStuff to this StupidSet
     * @param moreStuff a StupidSet
     * @return <code>true</code> if at least one item
     * is added
     */
    public boolean addAll(StupidSet<T> moreStuff)
    {
        int initialSize = elements.size();
        
        for (int i = 0; i < moreStuff.elements.size(); i++){
            if (!contains(moreStuff.elements.get(i))){
                add(moreStuff.elements.get(i));
            }
        }
        if (initialSize == size){
            return false;
        }
        return true;
    }
    /**
     * This makes a Python-list style representation of 
     * our StupidSet.
     * @return a representation of the form
     * <pre>[one, two, three .... last]</pre>
     */
    public String toString()
    {
        /*
        String out = "[";
        for (int i = 0; i < size; i++){
            out += str();
        }
        out += "]";
        */
        String out = elements.toString();
        return out;
    }

    public int size()
    {
        return size;
    }
    public static void main(String[] args){
        StupidSet<Integer> set1 = new StupidSet <>();
        StupidSet<Integer> set2 = new StupidSet <>();
        int count = 1;
        do{
            if (count<4){
                set1.add(count);
            } else{
                set2.add(count);
            }
            count++;
        } while(count < 7);
        System.out.println("Inital set1: " + set1.toString());
        System.out.println("Inital set2: " + set2.toString());
        System.out.println("set1 added 1: " + set1.add(1));
        System.out.println("set2 added 6: " + set2.add(1));
        System.out.println("Current set1: " + set1.toString());
        System.out.println("Current set2: " + set2.toString());
        System.out.println("set1 contains 6: " + set1.contains(6));
        System.out.println("set2 contains 6: " + set2.contains(6));
        System.out.println("set1 contains all of set 2: " + set1.containsAll(set2));
        System.out.println("set2 contains all of set 1: " + set2.containsAll(set1));
        System.out.println("set1 adds all of set 2: " + set1.addAll(set2));
        System.out.println("set2 adds all of set 1: " + set2.addAll(set1));
    }
}