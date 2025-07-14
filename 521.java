class Solution {
    public int findLUSlength(String a, String b) {
        // time: O(n), space: O(1)
        if (a.equals(b)) {
            return -1;
        }
        else {
            return Math.max(a.length(), b.length());
        }
    }
}