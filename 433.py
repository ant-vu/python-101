class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # time: O(n * 8 * 4), space: O(n)
        s = set(bank)
        if endGene not in s and startGene != endGene:
            return -1
        q = deque([(startGene, 0)])
        visited = {startGene}
        while q:
            curGene, depth = q.popleft()
            if curGene == endGene:
                return depth
            for i in range(8):
                for j in 'ACGT':
                    if curGene[i] != j:
                        newGene = curGene[:i] + j + curGene[i+1:]
                        if newGene in s and newGene not in visited:
                            visited.add(newGene)
                            q.append((newGene, depth + 1))
        return -1