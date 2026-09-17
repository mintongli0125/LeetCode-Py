class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            tofind = target-num
            if tofind in hashmap:
                return(hashmap[tofind], i)
            else:
                hashmap[num] = i
