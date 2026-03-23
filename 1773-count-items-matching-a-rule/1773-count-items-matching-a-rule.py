class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
    # Ánh xạ ruleKey sang chỉ số trong mảng item
        key_index = {"type": 0, "color": 1, "name": 2}
    
        count = 0  # Biến đếm số phần tử phù hợp
        for item in items:
        # Nếu giá trị tại vị trí tương ứng bằng ruleValue thì tăng count
            if item[key_index[ruleKey]] == ruleValue:
                count += 1
        return count