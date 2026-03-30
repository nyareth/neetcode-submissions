class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        container = []
        for c in s:
            container.append(c.lower())
        
        for x in t:
            if x.lower() in container:
                del container[container.index(x)]
            else:
                return False
        if len(container) == 0:
            return True
        return False    
        