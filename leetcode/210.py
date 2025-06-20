class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(V + E), space: O(V + E)
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        res = []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for neighbor in graph[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []