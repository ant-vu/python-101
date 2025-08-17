class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # time: O(n), space: O(n)
        def isWin(X):
            return (([0,0] in X and [1,1] in X and [2,2] in X) or 
                    ([0,2] in X and [1,1] in X and [2,0] in X) or
                    ([0,0] in X and [0,1] in X and [0,2] in X) or
                    ([1,0] in X and [1,1] in X and [1,2] in X) or
                    ([2,0] in X and [2,1] in X and [2,2] in X) or
                    ([0,0] in X and [1,0] in X and [2,0] in X) or
                    ([0,1] in X and [1,1] in X and [2,1] in X) or
                    ([0,2] in X and [1,2] in X and [2,2] in X))

        isA = True
        A = []
        B = []
        for m in moves:
            if isA:
                A.append(m)
                if isWin(A):
                    return 'A'
                isA = False
            else:
                B.append(m)
                if isWin(B):
                    return 'B'
                isA = True
        return "Draw" if len(moves) == 9 else "Pending"