import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2counts = {}
        for i in nums:
            num2counts[i] = num2counts.get(i, 0) + 1
        freqs = []
        for key, val in num2counts.items():
            freqs.append((val,key))
        heap = []
        for f in freqs:
            heapq.heappush(heap,f)
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]



