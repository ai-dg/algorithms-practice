class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index_nums1 = m - 1
        index_nums2 = n - 1
        index_write = m + n - 1

        while index_nums2 >= 0:
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[index_write] = nums1[index_nums1]
                index_nums1 -= 1
            else:
                nums1[index_write] = nums2[index_nums2]
                index_nums2 -= 1

            index_write -= 1
        



        

def main():
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)


    

if __name__ == "__main__":
    main()