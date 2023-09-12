public class HourlyEmployee extends Employee{
    
    private double rate;
    public HourlyEmployee(String first, String last, String UNI_ID, String title, double rate) {
        super(last, first, UNI_ID, title);
        this.rate = rate;       
    }
    public double computeRegularPay(){
        return rate*40;
    }
    
}