class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time: O(V + E), space: O(V + E)
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()

        def dfs(course):
            if not graph[course]:
                return True
            elif course in visited:
                return False
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            graph[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True