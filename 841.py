class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # time: O(m + n), space: O(n)
        seen = [True] + [False] * (len(rooms) - 1)
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)

        # time: O(n^2), space: O(n)
        # taken = [0]
        # flg = True
        # while flg:
        #     cnt = 0
        #     for i in range(len(rooms)):
        #         if i in taken and set(taken) != set(taken + rooms[i]):
        #             for j in rooms[i]:
        #                 if j not in taken:
        #                     taken.append(j)
        #                     cnt = 1
        #     if not cnt:
        #         flg = False
        # return len(taken) == len(rooms)