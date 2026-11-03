class Solution:

    def encode(self, strs: List[str]) -> str:
        merged = ""
        for string in strs:
            merged = merged + string + "|-"
        return merged

    def decode(self, s: str) -> List[str]:
        
        arr = []
        count = 0
        for i, char in enumerate(s):
            next_char = s[i + 1] if i + 1 < len(s) else None
            if char == "|" and next_char == "-":
                if arr:
                    arr.append(s[i+1-count:i])
                else:
                    arr.append(s[i-count:i])
                count = 0
                continue
            count += 1
        return arr