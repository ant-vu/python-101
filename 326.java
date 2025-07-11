class Solution {
    public boolean isPowerOfThree(int n) {
        // time: O(1), space: O(1)
        return n > 0 ? Math.pow(3, 19) % n == 0 : false;
    }
}