#https://leetcode.com/problems/unique-paths/?envType=problem-list-v2&envId=math


#C(total, down) = total! / (down! * right!)
import math
class Solution(object):
    def uniquePaths(self, m, n):
        
        total = m + n - 2
        down = m - 1
        right = n - 1
        
        return math.factorial(total) // (math.factorial(down) * math.factorial(right))
