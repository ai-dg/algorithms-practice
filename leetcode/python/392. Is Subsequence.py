class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        index_s = 0
        

        for char_t in t:
            if index_s < len(s):
                if char_t == s[index_s]:
                    index_s += 1

        if index_s == len(s):
            return True

        
        

        return False        

if __name__ == "__main__":
    solution = Solution()

    s = "abc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))


    s = "axc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))


    s = "b"
    t = "c"
    print(solution.isSubsequence(s, t))

    s = ""
    t = "ahbgdcc"
    print(solution.isSubsequence(s, t))


    s = "ab"
    t = "baab"
    print(solution.isSubsequence(s, t))
        
    


        