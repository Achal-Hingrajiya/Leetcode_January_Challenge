class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = False
        
        if s == "":
            return 0
        
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        res = ""
        
        for c in s:
            if c.isdigit():
                res += c
            else: 
                break
            
        if res == "":
            return 0
   
        ans = int(res)
        
        if negative:
            ans = -ans
        
        return max(min(ans,2**31 -1),-2**31)
            
                