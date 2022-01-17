class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        d = dict()
        
        for i in range(len(pattern)):
            item = d.get(pattern[i])
            if not item:
                if arr[i] in d.values():
                    return False
                d[pattern[i]] = arr[i]
            else:
                if item != arr[i]:
                    return False
            
        return True