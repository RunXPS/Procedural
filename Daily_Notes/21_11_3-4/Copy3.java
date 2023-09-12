import java.nio.file.Path;
import java.nio.file.Files;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

public class Copy3
{
    public static void main(String[] args)
    {   
        Path input = Path.of(args[0]);
        Path output = Path.of(args[1]);
        //try with resources
        try(
            BufferedReader reader = Files.newBufferedReader(input);
            BufferedWriter writer = Files.newBufferedWriter(output);
            
        )
        {
            
            reader.lines()
                  .forEach(line -> writer.write(line));
        }
        catch(IOException ex)
        {
            System.err.println("You have been mooned by an IOException.");
        }

    }   
}