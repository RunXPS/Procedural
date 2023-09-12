import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.function.Consumer;
import java.io.IOException;
//cd 2122\s1\compsci\DailyNotes\21_11_3

public class FancyCat{
    public static void main(String[] args) {
    //gets fileName
        String fileName = args[0];

        try (BufferedReader br = Files.newBufferedReader(Path.of(fileName));){
            br.lines()
            .forEach(System.out::println);
        }
        catch(IOException ex){
            System.err.println("Yer done fer");
        } 
    }
}
