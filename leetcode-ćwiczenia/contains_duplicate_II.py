# Too slow whe table have many values
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

def second_containsNearbyDuplicate(self, nums, k):
    seen = set()

    for i, num in enumerate(nums):
        if i > k:
            seen.remove(nums[i - k - 1])
        if num in seen:
            return True
        seen.add(num)

    return False
