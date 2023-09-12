import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
//cd 2122\s1\CompSci\DailyNotes\21_11_3-4

public class Cat {
   public static void main(String[] args) {
    //gets fileName
    String fileName = args[0];

    try {
        BufferedReader br = Files.newBufferedReader(Path.of(fileName));
        String line = "";
        while( (line = br.readLine())  != null){
            System.out.println(line);
        }
        br.close();
    }
    catch(IOException ex){
        System.err.println("Yer done fer");
    }

    // 1 - open a file
    // 2 - iterate through it and speq to standard output (stdout)
    // 3 - close file
    } 
}
