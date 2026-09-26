class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        numbers = []

        for fixed, number in enumerate(nums):

            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            
            left = fixed + 1
            right = len(nums) - 1
       

            while (left < right):
                total = nums[fixed] + nums[left] + nums[right]
                triplet = [nums[fixed], nums[left], nums[right]]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    numbers.append(triplet)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                


        return numbers



        


if __name__ == "__main__":
    solution = Solution()

    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))

    nums = [0,1,1]
    print(solution.threeSum(nums))

    nums = [0,0,0]
    print(solution.threeSum(nums))

    nums = [-100,-70,-60,110,120,130,160]
    print(solution.threeSum(nums))