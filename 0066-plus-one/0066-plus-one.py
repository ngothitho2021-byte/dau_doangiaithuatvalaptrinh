class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nho = 1  
        
       
        for i in range(len(digits) - 1, -1, -1):
            tong = digits[i] + nho
            digits[i] = tong % 10 
            nho = tong // 10  
            
            
            if nho == 0:
                break
        
        
        if nho > 0:
            digits.insert(0, nho)
        
        return digits