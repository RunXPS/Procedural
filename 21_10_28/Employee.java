public abstract class Employee extends Person {
    private String title;

    public Employee(String first, String last, String UNI_ID, String title) {
        super(last, first, UNI_ID);
        this.title = title;
    }
    public String getTitle(){
        return title;
    }
    public abstract double computeRegularPay();
    public String toString(){
        return String.format("%s, %s - %s : %s : $%.2f", getLast(), getFirst(), getUNI_ID(), getTitle(), computeRegularPay());
    }
}