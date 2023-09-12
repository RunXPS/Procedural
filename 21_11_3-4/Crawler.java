import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
//cd 2122\s1\compsci\DailyNotes\21_11_3-4

public class Crawler {
    public static void main(String[] args) {
        String directoryName = args[0];
        String extension = args[1];

        Path d1 = Path.of(directoryName);
            try {
            //Files.list(d1).filter(s -> s.toString().endsWith(extension)).forEach(System.out::println);
            Files.list(d1).forEach(System.out::println);
            } catch(IOException ex) {
                ex.printStackTrace();
            }   
    }//main
}//class