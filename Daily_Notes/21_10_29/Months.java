public class Months {
    private String[] name;
    public Months(){
        names = new String[]{"", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "Npvember", "December"};
    }
    public static void main(String[] args) {
        try {
            int n = Integer.parseInt(args[0]);
            Months mon = new Months();
            System.out.println(mon.names[n]);
        }
        /*
             --- BAD CODE ---
catches everything & makes no specific comments
        catch (Exception ex){
            System.err.println("I'm Dead");
        }
        */
        catch(NumberFormatException ex){
            System.err.pringln("Usage: java Months(number 1-12)");
        }
        catch(IndexOutOfBoundsException ex){
            System.err.println("Your number is out of bounds or you didn't enter an argumenet");
        }
        finally{
            // 'finally' runs unconditionally
            System.out.println("Thank you for using my brilliant Program");
        }
    }
}
