class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {
            i:[] for i in range(0,numCourses)
        }

        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        visited = set()
        cycle = set()
        res = []
        def rec(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            for p in adj[c]:
                if not rec(p):
                    return False
            res.append(c)
            cycle.remove(c)
            visited.add(c)
            return True
        
        for c in range(0, numCourses):
            if not rec(c):
                return []
        return res