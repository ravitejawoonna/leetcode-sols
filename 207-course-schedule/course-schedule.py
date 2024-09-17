class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {
            i:[] for i in range(numCourses)
        }

        for d in prerequisites:
            adj[d[0]].append(d[1])        
        
        visited = set()
        def rec(c):
            if c in visited:
                return False
            if adj[c] == []:
                return True
            
            visited.add(c)
            print(c)

            for p in adj[c]:
                if not rec(p): return False
            visited.remove(c)
            adj[c] = []
            return True
        
        for i in range(0, numCourses):
            if not rec(i): return False
        return True
