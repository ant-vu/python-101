class Solution {
    public boolean checkRecord(String s) {
        // time: O(n), space: O(1)
        int n = s.length();
        int cnt = 0, late = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'A') {
                cnt++;
                if (cnt >= 2) return false;
                late = 0;
            }
            else if (s.charAt(i) == 'L') {
                late++;
                if (late >= 3) return false;
            }
            else late = 0;
        }
        return true;
    }
}