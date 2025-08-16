class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # time: O(n), space: O(n)
        st = []
        for op in operations:
            if op == '+':
                st.append(st[-2] + st[-1])
            elif op == 'D':
                st.append(2 * st[-1])
            elif op == 'C':
                st.pop()
            else:
                st.append(int(op))
        return sum(st)