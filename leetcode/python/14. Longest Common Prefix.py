class Solution(object):

    def take_each_word(self, word1, word2, answer=""):

        if len(word1) == 0 or len(word2) == 0:
            return answer

        if word1[0] != word2[0]:
            return answer

        answer += word1[0]
        return self.take_each_word(word1[1:], word2[1:], answer)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1 or len(strs) > 200:
            return ""

        if len(strs) == 1:
            return strs[0]

        answer = strs[0]

        for word in strs[1:]:
            if len(word) == 0:
                return ""
            answer = self.take_each_word(answer, word)

            if answer == "":
                return ""
                    

        return answer


def main():
    solution = Solution()
    strs_1 = ["flower", "flow", "flight"]
    strs_2 = ["dog", "racecar", "car"]
    strs_3 = ["a"]
    strs_4 = ["",""]
    strs_5 = ["ab", "a"]
    strs_6 = ["flower","flower","flower","flower"]

    print(solution.longestCommonPrefix(strs_1))
    print(solution.longestCommonPrefix(strs_2))
    print(solution.longestCommonPrefix(strs_3))
    print(solution.longestCommonPrefix(strs_4))
    print(solution.longestCommonPrefix(strs_5))
    print(solution.longestCommonPrefix(strs_6))


if __name__ == "__main__":
    main()
