class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        area = 0
        area_max = 0

        while (left < right):

            number_left = height[left]
            number_right = height[right]

            if number_left <= number_right:
                area = height[left] * (right - left)
                left += 1
            elif number_left > number_right:
                area = height[right] * (right - left)
                right -= 1

            if area > area_max:
                area_max = area
            

        return area_max
        


if __name__ == "__main__":
    solution = Solution()

    nums = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(nums))

    nums = [1,1]
    print(solution.maxArea(nums))