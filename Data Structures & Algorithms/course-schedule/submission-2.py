class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * numCourses

        def dfs(node):
            # Found a cycle
            if state[node] == 1:
                return True

            # Already processed — no cycle here
            if state[node] == 2:
                return False

            # Mark as visiting
            state[node] = 1

            # Visit neighbors
            for nei in adjList[node]:
                if dfs(nei):
                    return True

            # Mark as fully processed
            state[node] = 2
            return False

        # Run DFS for all courses
        for i in range(numCourses):
            if state[i] == 0:
                if dfs(i):
                    return False  # cycle → cannot finish

        return True  # no cycle
