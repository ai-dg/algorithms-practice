class Solution(object):

    ROMAIN_CHARS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    ROMAIN_VALUES = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    def sum_values(self, s, answer = 0):

        if len(s) == 0:
            return answer

        if len(s) == 1:
            return answer + self.ROMAIN_VALUES[s[0]]
        

        int_char = self.ROMAIN_VALUES[s[0]]
        int_char_next = self.ROMAIN_VALUES[s[1]]


        if int_char >= int_char_next:
            return self.sum_values(s[1:], answer + int_char)
        else:
            return self.sum_values(s[2:], answer + (int_char_next - int_char))


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) <= 1 and len(s) >= 15:
            return 0

        if any(char not in self.ROMAIN_CHARS for char in s):
            return 0

        answer = self.sum_values(s)       



        return answer

        


def main():
    solution = Solution()
    s_1 = "III"
    s_2 = "LVIII"
    s_3 = "MCMXCIV"

    print(solution.romanToInt(s_1))
    print(solution.romanToInt(s_2))
    print(solution.romanToInt(s_3))


    




if __name__ == "__main__":
    main()