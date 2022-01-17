class Solution:
    def maxDistToClosest(self, arr: List[int]) -> int:

        n = len(arr)
        
        def closest_left(index):
            for i in range(index-1, -1, -1):
                if arr[i] == 1:
                    return i
            return -1

        def closest_right(index):
            for i in range(index + 1, n):
                if arr[i] == 1:
                    return i
            return -1
        
        pos = -float("inf")
        for i in range(n):
            if not arr[i]:
                left = closest_left(i)
                right = closest_right(i)
                d_right = float("inf")
                d_left = float("inf")
                if left != -1:
                    d_left = i - left
                if right != -1:
                    d_right = right - i

                distance = min(d_left, d_right)
                pos = max(pos, distance)
                
        return pos