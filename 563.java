/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int totalTilt = 0;

    public int findTilt(TreeNode root) {
        // time: O(n), space: O(n)
        this.valueSum(root);
        return this.totalTilt;
    }

    protected int valueSum(TreeNode node) {
        if (node == null)
            return 0;
        int lSum = this.valueSum(node.left);
        int rSum = this.valueSum(node.right);
        int tilt = Math.abs(lSum - rSum);
        this.totalTilt += tilt;
        return node.val + lSum + rSum;
    }
}