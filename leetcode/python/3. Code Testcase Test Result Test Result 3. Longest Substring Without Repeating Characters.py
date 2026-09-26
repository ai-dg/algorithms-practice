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

        # Recursion method in python O(n)
        def recursivite(s, index, letters, temp, double):
            
            # Go back at the end of the string
            if index >= len(s):
                if len(temp) > len(letters):
                    letters.clear()
                    letters.extend(temp)
                return

            # Removing until repeated letter
            while s[index] in double:
                removed = temp.popleft()
                # Unordered list to check doubles
                double.remove(removed)

            # Adding each character into temp
            temp.append(s[index])            
            double.add(s[index])

            # Adding the biggest sequence without repetition into letters list
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