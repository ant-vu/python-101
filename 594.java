class Solution {
    public int findLHS(int[] nums) {
        // time: O(n), space: O(n)
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int n : nums) {
            freqMap.put(n, freqMap.getOrDefault(n, 0) + 1);
        }
        int res = 0;
        for (int n : freqMap.keySet()) {
            if (freqMap.containsKey(n + 1)) {
                res = Math.max(res, freqMap.get(n) + freqMap.get(n + 1));
            }
        }
        return res;
    }
}