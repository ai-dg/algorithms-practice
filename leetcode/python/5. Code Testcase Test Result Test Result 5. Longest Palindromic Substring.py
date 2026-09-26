# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_final = ""

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(sub_final):
                    sub_final = s[left:right + 1]
                left -= 1
                right += 1


            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(sub_final):
                    sub_final = s[left:right + 1]
                left -= 1
                right += 1

        return sub_final





def main():
    s = "cbbd"

    sol = Solution()
    # print("test")

    print(s[:2])

    sub = sol.longestPalindrome(s)

    print(f"s: {s}")
    print(sub)



if __name__ == "__main__":
    main()