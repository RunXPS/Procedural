import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.TreeMap;
import java.io.BufferedReader;

public class Final {
    public static String clean(String input){
        String out = "";
        for (int i = 0; i < input.length(); i++){
            if (Character.isLetterOrDigit(input.charAt(i)) || input.charAt(i) == '\''){
                out += input.charAt(i);
            }
        }
        return out;
    }
    public static ArrayList sortAdd (Arraylist words, String word){
        while (!(words.contains(word))){
            for (int i = 0; i < words.size(); i++){
                String current = words.get(i);
                if (current.charAt(0) == word.charAt(0)){
                    for (int j = 1; j < current.size(); j++){

                    }
                }
            }
        }
        return words;
    }
    public static void main(String[] args) {
        String fileName = args[0];
        TreeMap<String, Integer> list = new Treemap<>();
        try {
            BufferedReader br = Files.newBufferedReader(Path.of(fileName));
            String line = "";
            while( (line = br.readLine())  != null){
                String[] words = line.split(" ");
                for (int i = 0; i < words.length; i++){
                    String current = clean(words[i].toLowerCase());
                    if (list.get(current) != null){
                        list.replace(current, list.get(current)+1);
                    } else {
                        list.put(current,1);
                    }
                }
            }
            br.close();
            for (int i = 0; i<countList.size(); i++){
                System.out.println(wordList.get(i) + ": " + countList.get(i));
            }
        }
        catch(IOException ex){
            System.err.println("--IO Exception--");
        }
    }
}
/*
        
        Path file = Path.of(filename);
        String lines = List.of(Files.readAllLines(file));
        String[][] words = new String[1][2];
        System.out.println("--Filler--");
*/