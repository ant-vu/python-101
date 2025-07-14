import java.util.regex.Pattern;

class Solution {
    public boolean detectCapitalUse(String word) {
        // time: O(n), space: O(n)
        return Pattern.matches("([A-Z]+|[a-z]+|[A-Z][a-z]*)", word);
    }
}