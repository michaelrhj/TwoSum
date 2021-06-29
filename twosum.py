class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for counterFirst in range(len(nums)):
            for counterSecond in range(1,len(nums)):
                total = nums[counterFirst] + nums[counterSecond]
                if total == target and counterFirst!=counterSecond:
                    return(counterFirst,counterSecond)
