public class Exercises
{
    public static void main(String[] args)
    {
        System.out.println(between("catamaran", 'a').equals("tamar"));
        System.out.println(between("catamaran", 'c').equals(""));
        System.out.println(between("catamaran", 'q').equals(""));
        System.out.println(laxEquals("    boot", "boot"));
        System.out.println(laxEquals("boot    ", "boot"));
        System.out.println(laxEquals("     boot    ", "boot"));
        System.out.println(laxEquals(" \t\n    boot \n\t   ", "boot"));
        System.out.println(getExtension("wd2.tex").equals("tex"));
        System.out.println(getExtension("hello.py").equals("py"));
        System.out.println(getExtension("Hello.java").equals("java"));
        System.out.println(getExtension("tossMeNow").equals(""));
        System.out.println(getExtension(".").equals(""));
        System.out.println(isUpperCaseOnly("EAT NOW 123"));
        System.out.println(!isUpperCaseOnly("eat NOW 123"));
        System.out.println(isUpperCaseOnly(""));
    }
    /*
     * This returns an empty string if q is not present in
     * s or if it only appears once.  Otherwise, it returns the
     * substring between the first and last instances of q in s.
     */
    public static String between(String s, char q)
    {
        s.indexOf(q);
        int first = s.indexOf(q);
        int last = s.lastIndexOf(q);

        if (first < 0 || last < 0 || first == last){
            return "";
        }
        return s.substring(first + 1, last);
    }
    /*
     * This returns true if the only difference between s1 and s2
     * is leading or trailing whitespace.  
     */
    public static boolean laxEquals(String s1, String s2)
    {
        if (s1.strip().equals(s2.strip())){
            return true;
        }
        return false;
    }
    /*
     * this returns an empty string if the fileName is empty
     * or has no extension. Otherwise, it returns the extension
     * without the dot.
     */
    public static String getExtension(String fileName)
    {

        if (fileName == "" || fileName.lastIndexOf(".") == -1){
            return "";
        }
        return fileName.substring(fileName.lastIndexOf(".") + 1, fileName.length());
    }
    /*
     * this returns true if the String contains only uppercase
     * or non-alpha characters.
     */
    public static boolean isUpperCaseOnly(String s)
    {
        if (s.toUpperCase() == s){
            return true;
        }
        return false;
    }
}