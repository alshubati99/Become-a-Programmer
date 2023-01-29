package main;
public class Hangman{
    public int countAlphabet (String word, char alphabet) {
        // Auto-generated method stub:
        int result = 0;
        for (char c: word.toCharArray()){
            if(c== alphabet) result ++;
        }
        return result;
    }
}