class Solution {
    public int countSegments(String s) {
        // time: O(n), space: O(1)
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if ((i == 0 || s.charAt(i - 1) == ' ') && s.charAt(i) != ' ') {
                cnt++;
            }
        }
        return cnt;
    }
}