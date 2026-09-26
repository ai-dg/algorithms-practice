class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
     

        start  = 0
        end = len(s) - 1

        while (start < end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1



if __name__ == "__main__":
    solution = Solution()

    s = ["h","e","l","l","o"]
    solution.reverseString(s)
    print(s)


    s = ["H","a","n","n","a","h"]
    solution.reverseString(s)
    print(s)

    