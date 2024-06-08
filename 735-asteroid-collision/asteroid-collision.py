class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            
            stack.append(a)
            while stack:
                if len(stack) <= 1:
                    break

                last =  stack.pop()
                pen = stack.pop()

                if last < 0  and  pen > 0:
                    if abs(pen) == abs(last):
                        continue
                    else:
                        if abs(pen) > abs(last):
                            stack.append(pen)
                        else:
                            stack.append(last)
                else:
                    stack.append(pen)
                    stack.append(last)
                    break
        return stack