import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
         前 K 个高频元素
        """
        total= {}
        for num in nums:
            if num not in total:
                total[num] = 1
            total[num] += 1
        res, inner = [], []
        for key,value in total.items():
            heapq.heappush(inner, (-value, key))
        while k>0:
            res.append(heapq.heappop(inner)[1])
            k = k-1
        return res