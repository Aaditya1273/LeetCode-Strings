class Solution:
    def romanToInt(self, s):
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                  'C': 100, 'D': 500, 'M': 1000} 
        t = 0
        i = 0
        
        while i < len(s):
            if (i + 1 < len(s) and v[s[i]] < v[s[i+1]]):
                t += v[s[i+1]] - v[s[i]]
                i += 2
            else:
                t += v[s[i]]
                i += 1
                
        return t






# values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}

# s= input("enter sting: ")
# no=int(0)
# for i in range(0,len(s)):
#     no=no+s