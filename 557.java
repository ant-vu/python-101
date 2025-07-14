class Solution {
    public String reverseWords(String s) {
        // time: O(n), space: O(n)
        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder();
        for (String w : words) {
            StringBuilder revWord = new StringBuilder(w).reverse();
            res.append(revWord).append(" ");
        }
        res.deleteCharAt(res.length() - 1);
        return res.toString();
    }
}