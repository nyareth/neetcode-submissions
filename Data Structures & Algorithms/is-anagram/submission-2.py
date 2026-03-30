class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        container = []
        box = []
        for c in s:
            container.append(c)
        
        for x in t:
            box.append(x)
        
        box.sort()
        container.sort()
        if box == container:
            return True
        return False