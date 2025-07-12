class Solution {
    public int longestPalindrome(String s) {
        // time: O(n), space: O(1)
        Set<Character> charSet = new HashSet<>();
        int res = 0;
        for (char c : s.toCharArray()) {
            if (charSet.contains(c)) {
                charSet.remove(c);
                res += 2;
            }
            else {
                charSet.add(c);
            }
        }
        if (!charSet.isEmpty()) res++;
        return res;
    }
}