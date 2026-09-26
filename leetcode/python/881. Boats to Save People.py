class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while(left <= right):

            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            elif people[left] + people[right] > limit:
                right -= 1
                boats += 1
            
            

        return boats



if __name__ == "__main__":
    solution = Solution()

    people = [1,2]
    limit = 3
    print(solution.numRescueBoats(people, limit))

    people = [3,2,2,1]
    limit = 3
    print(solution.numRescueBoats(people, limit))

    people = [3,5,3,4]
    limit = 5
    print(solution.numRescueBoats(people, limit))

    people = [2,2]
    limit = 6
    print(solution.numRescueBoats(people, limit))


    people = [7,3,2]
    limit = 8
    print(solution.numRescueBoats(people, limit))
    