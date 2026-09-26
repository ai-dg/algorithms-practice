

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)


        left = 0
        right = len(nums) - 1
        write = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[write] = left_square
                left += 1
            else:
                result[write] = right_square
                right -= 1

            write -= 1

        return result
        


if __name__ == "__main__":
    solution = Solution()

    nums = [-4,-1,0,3,10]
    print(solution.sortedSquares(nums))
    


    nums = [-7,-3,2,3,11]
    print(solution.sortedSquares(nums))
    

  