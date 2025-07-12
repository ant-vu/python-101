class Solution {
    public String toHex(int num) {
        // time: O(1), space: O(1)
        if (num == 0) return "0";
        StringBuilder str = new StringBuilder();
        char[] h = "0123456789abcdef".toCharArray();
        while (num != 0) {
            int r = num & 15;
            str.append(h[r]);
            num >>>= 4;
        }
        return str.reverse().toString();
    }
}