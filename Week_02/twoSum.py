class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        两数之和
        """
        record = {}
        for i in range(len(nums)):
            if record.get(target-nums[i]) is not None:
                return [record.get(target-nums[i]), i]
            record[nums[i]] = i