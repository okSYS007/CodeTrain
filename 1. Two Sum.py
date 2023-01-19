
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

nums1 = [2,11,7,15]
target1 = 9 
nums2 = [3,2,4]
target2 = 6
nums3 = [3,2,4]
target3 = 6
nums4 = [4,5,2]
target4 = 6


MySolution = Solution()
print(MySolution.twoSum(nums1, target1))#[0,1] Because nums[0] + nums[1] == 9, we return [0, 1].
print(MySolution.twoSum(nums2, target2))#[1,2]
print(MySolution.twoSum(nums3, target3))#[0,1]
print(MySolution.twoSum(nums4, target4))#[0,2]
