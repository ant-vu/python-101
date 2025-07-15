class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        // time: O(m * n), space: O(m * n)
        int m = mat.length;
        int n = mat[0].length;
        int reshape[][] = new int[r][c];
        if (m * n == r * c) {
            for (int i = 0; i < m * n; i++) {
                reshape[i / c][i % c] = mat[i / n][i % n];
            }
        }
        else {
            reshape = mat;
        }
        return reshape;
    }
}