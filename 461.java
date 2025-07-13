class Solution {
    public int hammingDistance(int x, int y) {
        // time: O(1), space: O(1)
        int hamming = 0;
        int xor = x ^ y;
        while (xor != 0) {
            if ((xor & 1) == 1) {
                hamming++;
            }
            xor >>= 1;
        }
        return hamming;
    }
}