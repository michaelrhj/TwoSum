class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False
        for counterFirst in range(0,len(nums)):
            counterSecond = counterFirst+1
            while found == False or counterSecond<len(nums):
                total = nums[counterFirst] + nums[counterSecond]
                if total == target:
                    found = True
                    return(counterFirst,counterSecond)
                else:
                    counterSecond = counterSecond+1