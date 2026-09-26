class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        clean = "".join(char for char in string if char.isalnum())
        if clean == "":
            return True

        half = len(clean) // 2
        first = clean[:half]
        clean = clean[::-1]
            
        second = clean[:half]



        for index in range(len(first)):
            if first[index] != second[index]:
                return False

        return True

        



if __name__ == "__main__":
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))


    s = "race a car"
    print(solution.isPalindrome(s))
    

    s = " "
    print(solution.isPalindrome(s))

    s = "0P"
    print(solution.isPalindrome(s))
    


        





        