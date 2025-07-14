class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // time: O(n), space: O(n)
        int[] res = new int[nums1.length];
        Stack<Integer> st = new Stack<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n : nums2) {
            while (!st.isEmpty() && n > st.peek()) {
                map.put(st.pop(), n);
            }
            st.add(n);
        }
        int i = 0;
        for (int n : nums1) {
            res[i++] = map.getOrDefault(n, -1);
        }
        return res;
    }
}