class Solution:
    def lengthOfLongestSubstring(self, s):
        p, i, q = {}, 0, 0
        for j, ch in enumerate(s):
            i = max(i, p.get(ch, -1) + 1)
            p[ch] = j
            q = max(q, j - i + 1)
        return q
 

#  class Solution:
#     def lengthOfLongestSubstring(self, s):
#         p = {}   
#         i = 0    
#         r = 0    
        
#         for j, q in enumerate(s):   
#             if q in p and p[q] >= i:
#                 i = p[q] + 1
#             p[q] = j
#             r = max(r, j - i + 1)
        
#         return r


