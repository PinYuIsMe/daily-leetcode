from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for i in adj[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if sum(indegree) == 0:
            return result
        else:
            return []
        

            
        