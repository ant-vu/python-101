class Solution {
    public int arrayPairSum(int[] nums) {
        // time: O(n), space: O(n)
        int cnt[] = new int[20001];
        for (int i = 0; i < nums.length; i++) {
            cnt[nums[i] + 10000]++;
        }
        boolean min = true;
        int sum = 0;
        for (int i = 0; i < cnt.length; i++) {
            while (cnt[i] > 0) {
                if (min) {
                    sum += i - 10000;
                }
                cnt[i]--;
                min = !min;
            }
        }
        return sum;
    }
}