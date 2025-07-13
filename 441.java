class Solution {
    public int arrangeCoins(int n) {
        // time: O(logn), space: O(1)
        long l = 1;
        long r = n;
        while (l <= r) {
            long m = l + (r - l) / 2;
            long coinsUsed = m * (m + 1) / 2;
            if (coinsUsed == n) {
                return (int) m;
            }
            else if (n < coinsUsed) {
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        return (int) r;
    }
}