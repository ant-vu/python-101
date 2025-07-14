class Solution {
    public String licenseKeyFormatting(String s, int k) {
        // time: O(n), space: O(1)
        int cnt = 0;
        int n = s.length();
        StringBuilder res = new StringBuilder();
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) != '-') {
                res.append(Character.toUpperCase(s.charAt(i)));
                cnt++;
                if (cnt == k) {
                    res.append('-');
                    cnt = 0;
                }
            }
        }
        if (res.length() > 0 && res.charAt(res.length() - 1) == '-') {
            res = new StringBuilder(res.substring(0, res.length() - 1));
        }
        res.reverse();
        return res.toString();
    }
}