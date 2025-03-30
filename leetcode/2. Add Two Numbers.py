# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getting_number(self, l):
        index = 1
        number = 0
        while l != None:
            value = l.val
            number += value * index
            index *= 10
            l = l.next
        return number
        
    def getting_reverse_list(self, number):
        number_to_add = int(number % 10)
        number = number // 10
        head = ListNode(number_to_add)
        current = head

        while number >= 1:
            number_to_add = int(number % 10)
            number = number // 10
            current.next = ListNode(number_to_add)
            current = current.next
        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number1 = self.getting_number(l1)
        number2 = self.getting_number(l2)
        total = number1 + number2
        return self.getting_reverse_list(total)

def filling_list(nums):
    start = ListNode()
    current = start

    for num in nums:
        current.next = ListNode(num)
        current = current.next
    
    return start.next
        
def main():
    l1 = filling_list([9,9,9,9,9,9,9])
    l2 = filling_list([9,9,9,9])
    answer = Solution()
    final_list = answer.addTwoNumbers(l1, l2)

if __name__ == "__main__":
    main()