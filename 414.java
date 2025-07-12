class Solution {
    public int thirdMax(int[] nums) {
        // time: O(n), space: O(1)
        TreeSet<Integer> sortedNums = new TreeSet<>();
        for (int n : nums) {
            if (sortedNums.contains(n)) {
                continue;
            }
            else if (sortedNums.size() == 3) {
                if (sortedNums.first() < n) {
                    sortedNums.pollFirst();
                    sortedNums.add(n);
                }
            }
            else {
                sortedNums.add(n);
            }
        }
        if (sortedNums.size() == 3) {
            return sortedNums.first();
        }
        return sortedNums.last();
    }
}