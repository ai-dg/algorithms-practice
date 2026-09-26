class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < -2^31 and x > 2^31:
            return False

        if x < 0:
            return False

        if x > 0 and x < 10:
            return True

        numbers = []

        x_temp = x
        while(x_temp):
            number = x_temp % 10
            x_temp = int(x_temp / 10)
            numbers.append(int(number))

        numbers_inversed = numbers[::-1]

        print(numbers)
        print(numbers_inversed)

        i = 0
        total = len(numbers)
        while(i <= total - 1):

            if numbers[i] != numbers_inversed[i]:
                return False
            i += 1

        return True

def main():
    solution = Solution()

    print(solution.isPalindrome(121))



if __name__ == "__main__":
    main()