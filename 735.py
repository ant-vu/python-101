class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        stack = []
        for i in asteroids:
            if not stack or (stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i < 0) or (stack[-1] < 0 and i > 0):
                stack.append(i)
            else:
                flg = False
                while stack:
                    if (stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i < 0) or (stack[-1] < 0 and i > 0):
                        break
                    elif abs(stack[-1]) == abs(i):
                        stack.pop()
                        flg = False
                        break
                    elif abs(stack[-1]) > abs(i):
                        flg = False
                        break
                    elif abs(stack[-1]) < abs(i):
                        stack.pop()
                        flg = True
                if flg:
                    stack.append(i)
        return stack