class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        
        if n != m:                          # length of both numbers are not same
            if n > m:
                b = (n-m)*"0" + b           # add leading zeros to b
            else:
                a = (m-n)*"0" + a           # add leading zeros to a
                
        N = len(a)                          # new length
        
        ans = ''
        carry = False
        
        for i in range(N-1, -1, -1):
            if a[i] == b[i] :               # both digits are same
                if a[i] == '1':             # both digits are 1
                    if carry:               # 1 + 1 + 1 -> 1 with carry
                        ans = '1' + ans
                        carry = True
                    else:                   # 1 + 1 -> 0 with carry
                        ans = '0' + ans
                        carry = True
                else:                       # both digits are 0
                    if carry:               # 0 + 0 + 1 -> 1 without carry
                        ans = '1' + ans
                        carry = False
                    else:                   # 0 + 0 -> 0
                        ans = '0' + ans
            
            else:                           # both digits are not same
                
                if carry:                   # 0 + 1 + 1 -> 0 with carry
                                            # 1 + 0 + 1 -> 0 with carry
                    ans = '0' + ans
                    carry = True
                    
                else:                       # 0 + 1 -> 1
                                            # 1 + 0 -> 1
                    ans = '1' + ans
        
        if carry :
            ans = '1' + ans
        
        return ans