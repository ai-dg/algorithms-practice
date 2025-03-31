# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        letters = []
        temp = deque()
        double = set()

        def recursivite(s, index, letters, temp, double):
            if index >= len(s):
                if len(temp) > len(letters):
                    letters.clear()
                    letters.extend(temp)
                return

            while s[index] in double:
                removed = temp.popleft()
                double.remove(removed)

            temp.append(s[index])            
            double.add(s[index])

            if len(temp) > len(letters):
                letters.clear()
                letters.extend(temp)

            return recursivite(s, index + 1, letters, temp, double)

        recursivite(s, index, letters, temp, double)
        return len(letters)


def main():
    s = "abcabcbb"
    solution_x = Solution()
    length = solution_x.lengthOfLongestSubstring(s)
    print(length)

if __name__ == "__main__":
    main()