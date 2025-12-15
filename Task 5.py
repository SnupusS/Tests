#https://leetcode.com/problems/rotate-array/?envType=problem-list-v2&envId=math

class Solution(object):
    def rotate(self, nums, k):
    
        n = len(nums)
        if n == 0:
            return
        
        k = k % n  

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
       
        reverse(0, n - 1)

        reverse(0, k - 1)
 
        reverse(k, n - 1)
