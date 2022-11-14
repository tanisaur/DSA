#Leet code 1480. Running Sum of 1d Array
#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #start range from the second index(1) in the array
        for i in range(1,n):
            nums[i] = nums[i-1] + nums[i]  
        return nums
