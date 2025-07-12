class Solution {
    public void reverseString(char[] s) {
        // time: O(n), space: O(1)
        int l = 0;
        int r = s.length - 1;
        while (l < r) {
            char tmp = s[r];
            s[r] = s[l];
            s[l] = tmp;
            l++;
            r--;
        }
    }
}