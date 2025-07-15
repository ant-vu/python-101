class Solution {
    public int distributeCandies(int[] candyType) {
        // time: O(n), space: O(n)
        Set<Integer> set = new HashSet<>();
        for (int i : candyType) set.add(i);
        return Math.min(set.size(), candyType.length / 2);
    }
}