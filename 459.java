class Solution {
    public boolean repeatedSubstringPattern(String s) {
        // time: O(n), space: O(n)
        String concat = s + s;
        return concat.substring(1, concat.length() - 1).contains(s);
    }
}