class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False

        mapping = {}
        mapping_rev = {}
        visited = set()

        for i in range(len(s)):
            code = pattern[i]
            word = s[i]
            # if i have seen this word already
            if word in visited:
                if mapping[word] != code:
                    return False
                else:
                    continue
            # if i have not seen word yet
            else:
                # but what if i have seen the code???
                if code in mapping_rev:
                    return False
                else:
                    mapping[word] = code
                    mapping_rev[code] = word
                    visited.add(word)

        return True