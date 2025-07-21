class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(V + E), space: O(V + E)
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()
        visiting = set()
        order = []

        def dfs(course):
            if course in visited:
                return True
            elif course in visiting:
                return False
            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order