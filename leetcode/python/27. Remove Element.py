class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        print(nums.count(val))

        for number in range(nums.count(val)):
            nums.remove(val)


        

        return len(nums)



def main():
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    print(f"{solution.removeElement(nums, val)}, nums = {nums}")

    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(f"{solution.removeElement(nums, val)}, nums = {nums}")



    

if __name__ == "__main__":
    main()