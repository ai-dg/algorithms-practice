
class Solution(object):
    s: str

    def is_there_a_number(self, s):
        for c in s:
            if c >= '0' and c <= '9':
                return True

        return False

    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """       
        length = len(s)
        while(self.is_there_a_number(s) == True):
            i = 0
            while(i < length):  
                if s[i] >= '0' and s[i] <= '9':
                    s = s.replace(s[i], "")
                    length = len(s)
                    if i > 0 and s[i - 1].isalpha() == True:
                        s = s.replace(s[i-1], "")
                        length = len(s)
                i += 1
        return s





def main():    
    
    s = "c5c"

    o = Solution()

    s = Solution.clearDigits(o, s)


    print(f"String: {s}")



    


if __name__ == "__main__":
    main()