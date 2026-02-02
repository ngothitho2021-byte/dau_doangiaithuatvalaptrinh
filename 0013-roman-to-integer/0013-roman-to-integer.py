class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        gia_tri = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
        ket_qua = 0
        
        
        for i in range(len(s)):
            
            hien_tai = gia_tri[s[i]]
            
           
            if i < len(s) - 1 and hien_tai < gia_tri[s[i + 1]]:
                ket_qua -= hien_tai  
            else:
                ket_qua += hien_tai  
        
       
        return ket_qua