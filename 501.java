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
    int maxStreak = 0;
    int curStreak = 0;
    int curNum = 0;
    List<Integer> res = new ArrayList();

    public int[] findMode(TreeNode root) {
        // time: O(n), space: O(n)
        dfs(root);
        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }
        return result;
    }

    public void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        dfs(node.left);
        int num = node.val;
        if (num == curNum) {
            curStreak++;
        } else {
            curStreak = 1;
            curNum = num;
        }
        if (curStreak > maxStreak) {
            res = new ArrayList();
            maxStreak = curStreak;
        }
        if (curStreak == maxStreak) {
            res.add(num);
        }
        dfs(node.right);
    }
}