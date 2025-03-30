# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def recursivite(index, reductions):
            if index >= len(nums):
                return []  
            result = target - nums[index]
            # Finding the number from value - target
            if result in reductions:
                return [reductions[result], index]
            reductions[nums[index]] = index
            return recursivite(index + 1, reductions)

        return recursivite(0, {})
    
def main():
    nums = [2,7,11,15]
    target = 9
    answer = Solution()
    list = answer.twoSum(nums, target)
    print(list)

if __name__ == "__main__":
    main()