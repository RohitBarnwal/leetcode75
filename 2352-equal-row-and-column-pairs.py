"""https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = Counter(tuple(row) for row in grid)
        count = 0
        for col in zip(*grid):  # transpose without building grid_t
            count += row_counter[tuple(col)]
        return count
