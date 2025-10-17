class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combined = s1 + " " + s2
        words = combined.split()
        seen = {}
        for w in words:
            if w in seen:
                seen[w] += 1
            else:
                seen[w] = 1
        result = []
        for word, count in seen.items():
            if count == 1:
                result.append(word)
        return result

