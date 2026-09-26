class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        read = 0
        write = 0

        while(read < len(nums)):


            if nums[write] == 0 and nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]

            if nums[write] != 0:
                write += 1


            read += 1
        


if __name__ == "__main__":
    solution = Solution()

    nums = [0,1,0,3,12]
    solution.moveZeroes(nums)
    print(nums)


    nums = [0]
    solution.moveZeroes(nums)
    print(nums)

    nums = [1,0,1]
    solution.moveZeroes(nums)
    print(nums)