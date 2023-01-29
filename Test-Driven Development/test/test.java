package test;
import java.beans.Transient;
public class test {
    @Test 
    void test_alphapetCountInWord(){
        String word = "pizza";
        char alphabet = 'a';
        Hangman hangman = new Hangman();
        int count = hangman.countAlphabet(word, alphabet);
        assertEquals(1, count);
    }
    
private void assertEquals(int i, int count) {
    }

}
    @Test 
    void test_lengthOfFetchWord(){
        Hangman hangman = new Hangman();
        String word = hangman.testWord();

        assertTrue(word.length()==5);
    }
