class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = []
        for n in nums:
            if n in cache:
                return True
            cache.append(n)
        return False