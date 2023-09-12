public class SalariedEmployee extends Employee{
    private double salary;
    public SalariedEmployee(String first, String last, String UNI_ID, String title, double salary) {
        super(last, first, UNI_ID, title);
        this.salary = salary;       
    }
    public double computeRegularPay(){
        return salary*40;
    }
}