class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // time: O(mlogm + nlogn), space: O(m + n)
        Arrays.sort(g);
        Arrays.sort(s);
        int contentChildren = 0;
        int idx = 0;
        while (contentChildren < g.length && idx < s.length) {
            if (g[contentChildren] <= s[idx]) {
                contentChildren++;
            }
            idx++;
        }
        return contentChildren;
    }
}