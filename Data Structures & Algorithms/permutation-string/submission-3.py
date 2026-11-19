class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Count = Counter(s1)
        windowLength = len(s1)
        s2Count = Counter(s2[0: windowLength])

        if s1Count == s2Count:
            return True
        
        for index in range(windowLength, len(s2)):
            s2Count[s2[index - windowLength]] -= 1
            s2Count[s2[index]] += 1
            if s1Count == s2Count:
                return True
        
        return False