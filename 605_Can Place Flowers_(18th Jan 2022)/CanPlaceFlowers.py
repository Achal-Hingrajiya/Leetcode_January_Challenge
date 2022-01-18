class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        N = len(arr)
        
        if n == 0:
            return True
        
        if N == 1:
            if n > 1 or arr[0]:
                return False
            else:
                return True
            
        if not arr[0] and not arr[1]:
            arr[0] = 1
            n -= 1
            
        if not arr[N-1] and not arr[N-2]:
            arr[N-1] = 1
            n -= 1   
            
        if n > 0:
            for i in range(1,N-1):
                if n == 0:
                    break
                if not arr[i]:
                    if not arr[i-1] and not arr[i+1]:
                        arr[i] = 1
                        n -= 1
        if n > 0:
            return False
        else:
            return True
                    