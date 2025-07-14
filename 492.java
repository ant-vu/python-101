class Solution {
    public int[] constructRectangle(int area) {
        // time: O(logn), space: O(1)
        int w = (int) Math.sqrt(area);
        while (area % w != 0) {
            w--;
        }
        int l = area / w;
        return (new int[] {l, w});
    }
}