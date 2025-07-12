class Solution {
    public char findTheDifference(String s, String t) {
        // time: O(m + n), space: O(1)
        char c = 0;
        for (char cs : s.toCharArray()) c ^= cs;
        for (char ct : t.toCharArray()) c ^= ct;
        return c;
    }
}