# Proper way is to have a code, but remember the length of the string before it, so we can determine whether the code is part of the string or not.

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word))+"_"+word
        print(s)
        return s
        

        # Hello5_World5_

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the underscore
            while s[j] != "_":
                j += 1

            # Extract the number
            length = int(s[i:j])

            # Extract the word
            word = s[j+1:j+1+length]
            res.append(word)

            # Move i to the beginning of the next encoded word
            i = j + 1 + length
        
        return res
