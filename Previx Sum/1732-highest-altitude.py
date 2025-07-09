"""https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # altitudes=[0]
        max_altitude = 0
        altitude=0
        for el in gain:
            altitude+=el
            max_altitude = max(max_altitude, altitude)
            # altitudes.append(altitude)
        return max_altitude
        