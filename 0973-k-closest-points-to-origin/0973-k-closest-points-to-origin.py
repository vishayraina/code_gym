# a max heap of the closest k points
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-(p[0]**2+p[1]**2)**(1/2), p)  for p in points]
        heap = []
        for p in points:
            heapq.heappush(heap, p)
            if len(heap) > k:
                heapq.heappop(heap)
        return [p[1] for p in heap]