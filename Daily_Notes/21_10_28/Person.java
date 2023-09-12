public abstract class Person {   
    private String last;
    private String first;
    private final String UNI_ID;
    public Person(String first, String last, String UNI_ID){
        this.first = first;
        this.last = last;
        this.UNI_ID = UNI_ID;
    }
    public String getLast(){
        return last;
    }
    public String getFirst(){
        return first;
    }
    public String getUNI_ID(){
        return UNI_ID;
    }
}