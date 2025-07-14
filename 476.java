class Solution {
    public int findComplement(int num) {
        // time: O(1), space: O(1)
        int bitLength = Integer.toBinaryString(num).length();
        int mask = (1 << bitLength) - 1;
        return num ^ mask;
    }
}