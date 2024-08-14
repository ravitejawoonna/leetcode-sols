class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def rec(arr, o, c):
            if len(arr) == 2 * n:
                res.append(arr)
                return
            
            if o < n:
                rec(arr + "(", o+1, c)
            if c < n and o > c:
                rec(arr + ")", o, c+1)
        
        rec("(", 1, 0)
        return res