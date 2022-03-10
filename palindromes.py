import math 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #checks if x negative
        if(x < 0):
            return False
        elif(x < 10):        #checks if its single digit
            return True
        
        #this singles out the digits into a list
        lst = []
        total = 0
        mod = 10
        
        if(x % 10 == 0): #do something different for 10's
            digit = x / 10
            while(digit > 10):
                digit = digit / 10
            lst.append(digit)
        else:
            digit = x % mod
            lst.append(round(digit))
        
        while x != total:
            mod = mod * 10
            total = (x % mod)
            digit = (total - 1) / (mod / 10)
            lst.append(math.floor(digit))

        #compares the beginning all the way to the end

        j = len(lst) - 1
        palindrome = True
        for i in range(len(lst)):
            if(lst[i] == lst[j]):
                j -= 1
            else:
                palindrome = False
                
        return palindrome
