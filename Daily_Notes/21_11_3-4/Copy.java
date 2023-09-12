import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.function.Consumer;
import java.io.IOException;
//cd 2122\s1\compsci\DailyNotes\21_11_3

public class Copy {
    public static void main(String[] args) {
        Path input = Path.of(args[0]);
        Path output = Path.of(args[1]);
        //try with resources
        try (
            BufferedReader reader = Files.newBufferedReader(input);
            BufferedWriter writer = Files.newBufferedWriter(output);
        ){
            reader.lines().forEach(line -> {
                try {
                    writer.write(line + "\n");
                }
            }};
        }//
        catch(IOException ex){
            System.err.println("You've been mooned by an IO exception");
        } //catch io
    }//main
}//class
