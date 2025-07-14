class Solution {
    public String[] findRelativeRanks(int[] score) {
        // time: O(m + n), space: O(n)
        int N = score.length;
        int M = findMax(score);
        int[] scoreToIdx = new int[M + 1];
        for (int i = 0; i < N; i++) {
            scoreToIdx[score[i]] = i + 1;
        }
        final String[] MEDALS = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        String[] ranks = new String[N];
        int place = 1;
        for (int i = M; i >= 0; i--) {
            if (scoreToIdx[i] != 0) {
                int originalIdx = scoreToIdx[i] - 1;
                if (place < 4) {
                    ranks[originalIdx] = MEDALS[place - 1];
                }
                else {
                    ranks[originalIdx] = String.valueOf(place);
                }
                place++;
            }
        }
        return ranks;
    }

    private int findMax(int[] score) {
        int maxScore = 0;
        for (int s : score) {
            if (s > maxScore) {
                maxScore = s;
            }
        }
        return maxScore;
    }
}