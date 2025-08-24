class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # time: O(nlogn + nm), space: O(n)
        myMat = [(sum(mat[i]), i) for i in range(len(mat))]
        myMat.sort()
        return [myMat[i][1] for i in range(k)]