def twoSum(nums, target):
    for i in range(len(nums) - 1):
        if target - nums[i] in nums[i+1:]:
            return [i, nums[i+1:].index(target - nums[i]) + i + 1]

def NativetwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
