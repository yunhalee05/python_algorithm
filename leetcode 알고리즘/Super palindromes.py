class Solution(object):        
    

    def superpalindromesInRange(self, left, right):
        count = 0
        leftnum = int(left)
        rightnum = int(right)
        MAX = 100000
        
        def reverse(a):
            result = 0
            while(a>0):
                result = result*10 + a%10
                a /=10
            return result

        def is_palindrome(a):
            return a == reverse(a)

        
        for i in range(MAX):
            k = str(i)
            t = k + k[-2::-1]
            v = int(t)**2
            
            if v>rightnum:
                break
            elif v>=leftnum and is_palindrome(v):
                count+=1
        
        for j in range(MAX):
            k = str(j)
            t = k+k[::-1]
            v = int(t)**2
            
            if v>rightnum:
                break
            elif v>=leftnum and is_palindrome(v):
                count+=1
                
                
        return count
            