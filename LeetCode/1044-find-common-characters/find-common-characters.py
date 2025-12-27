class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)   

        result = []
        for ch, freq in common.items():
            result.extend([ch] * freq)

        return result
