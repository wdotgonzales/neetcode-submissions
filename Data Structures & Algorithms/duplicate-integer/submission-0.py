from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        
        for number, count in count.items():
            if count > 1:
                return True

        return False
        