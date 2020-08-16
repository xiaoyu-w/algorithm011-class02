class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        数组的相对排序
        """
        arr = [0 for _ in range(1001)]
        res = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                res.append(arr2[i])
                arr[arr2[i]] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                res.append(i)
                arr[i] -= 1
        return res