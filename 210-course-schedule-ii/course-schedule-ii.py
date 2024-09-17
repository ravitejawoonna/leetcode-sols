class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {
            i:[] for i in range(0,numCourses)
        }

        for d in prerequisites:
            adj[d[0]].append(d[1])
        
        visited = set()
        output = []
        cycle = set()

        def rec(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            for p in adj[c]:
                if not rec(p): return False
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True
        
        for c in range(0, numCourses):
            if not rec(c):
                return []
        return output
            