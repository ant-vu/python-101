class Solution {
    public boolean isPowerOfFour(int n) {
        // time: O(1), space: O(1)
        return n > 0 ? Math.log(n) / Math.log(4) % 1 == 0 : false;
    }
}