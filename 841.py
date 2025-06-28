class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # time: O(n^2), space: O(n)
        taken = [0]
        flg = True
        while flg:
            cnt = 0
            for i in range(len(rooms)):
                if i in taken and set(taken) != set(taken + rooms[i]):
                    for j in rooms[i]:
                        if j not in taken:
                            taken.append(j)
                            cnt = 1
            if not cnt:
                flg = False
        return len(taken) == len(rooms)