class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()      # smaller asteroid explodes
                    continue
                elif stack[-1] == -ast:
                    stack.pop()      # both explode
                break
            else:
                stack.append(ast)    # no collision
        
        return stack