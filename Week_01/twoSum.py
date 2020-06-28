class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        temp = sorted(nums.copy())
        while i<j:
            if temp[i] + temp[j] == target:
                break
            elif temp[i] + temp[j] > target:
                j = j-1
            else:
                i = i+1
        i = nums.index(temp[i])
        nums.pop(i)
        j = nums.index(temp[j])
        if j>=i:
            j = j+1
        return [i,j]