"""https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            while stack and curr < 0 < stack[-1]:
                if abs(curr) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(curr) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(curr)
        return stack
