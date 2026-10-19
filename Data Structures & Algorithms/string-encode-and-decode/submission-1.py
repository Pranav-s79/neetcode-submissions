class Solution:

    def encode(self, strs: List[str]) -> str:
        
        str_output = ""
        for st in strs:
            str_output += str(len(st)) + "#" + st

            #format: len + # + string
        #empty string case:
        # "0#""
        return str_output

    def decode(self, s: str) -> List[str]:
        #test example: 5#Hello0#5#World7#abc#12312#abcdefghijkl1#!
        result = []
        i = 0

        #captures length, and ends on delimiter
        while i<len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            result.append(s[j+1: j+length+1])
            i = j+1+length


        return result
