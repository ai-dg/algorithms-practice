# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List

class Solution:
    # This is not an O(log(m + n)) method, just a simple solution to this problem
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        numbers = []
        numbers.extend(nums1)
        numbers.extend(nums2)      
        numbers.sort()
        length = len(numbers)
        median = 0
        if length % 2 == 0:
            index_1 = int((length / 2) + 0.5)
            index_2 = int((length / 2) - 0.5)
            median = (numbers[index_1] + numbers[index_2]) / 2
        else:
            median = numbers[int(length / 2)]
        return median
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    #     if len(nums1) > len(nums2):
    #         nums1, nums2 = nums2, nums1
        
    #     m, n = len(nums1), len(nums2)
    #     half = (m + n) // 2

    #     low = 0
    #     high = m

    #     while low <= high:
    #         i = (low + high) // 2
    #         j = half - i

    #         nums1_left = nums1[i - 1] if i > 0 else float('-inf')
    #         nums1_right = nums1[i] if i < m else float('inf')

    #         nums2_left = nums2[j - 1] if j > 0 else float('-inf')
    #         nums2_right = nums2[j] if j < n else float('inf')

    #         if nums1_left <= nums2_right and nums2_left <= nums1_right:
    #             if (m + n) % 2 == 0:
    #                 return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
    #             else:
    #                 return min(nums1_right, nums2_right)
    #         elif nums1_left > nums2_right:
    #             high = i - 1
    #         else:
    #             low = i + 1

    

        # numbers.sort() 

def main():
    nums1 = [1, 3]
    nums2 = [2, 4, 5 ,6]
    answer = Solution()
    number = answer.findMedianSortedArrays(nums1, nums2)
    print(f"median: {number}")

if __name__ == "__main__":
    main()