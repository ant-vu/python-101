class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        // time: O(n), space: O(1)
        int minM = m;
        int minN = n;
        for (int i = 0; i < ops.length; i++) {
            if (ops[i][0] < minM) {
                minM = ops[i][0];
            }
            if (ops[i][1] < minN) {
                minN = ops[i][1];
            }
        }
        return minM * minN;
    }
}