from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the idea is to find a duplicate that is within k steps of a value
        # we use a dict for keeping only the last indexes with that value
        # as older values are clearly not in the desired number of steps
        memo = {}

        for i in range(len(nums)):
            if nums[i] not in memo:
                memo[nums[i]] = i
            else:
                j = memo[nums[i]]
                if nums[j] == nums[i] and abs(i - j) <= k:
                    return True
                memo[nums[i]] = i

        return False