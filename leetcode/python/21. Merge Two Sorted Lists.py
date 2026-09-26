# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def full_values(values: list):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def count_number(list : ListNode):
    count = 0

    current = list

    while(current):
        count += 1
        current = current.next

    return count


def check_values_in_list(list: ListNode):

    current = list
    while(current):
        if current.val < -100 or current.val > 100:
            return False

        current = current.next

    return True


def recursive_sorting(list1 : ListNode, list2 : ListNode):

    if not list1 or not list2:
        return list1 or list2

    if list1.val <= list2.val:
        list1.next = recursive_sorting(list1.next, list2)

        return list1

    else:
        list2.next = recursive_sorting(list1, list2.next)

        return list2


class Solution(object):
    def mergeTwoLists(self, list1 : ListNode, list2 : ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2

        if not list2:
            return list1

        if count_number(list1) < 0 or count_number(list1) > 50:
            return []

        if count_number(list2) < 0 or count_number(list2) > 50:
            return []

        if check_values_in_list(list1) == False or check_values_in_list(list2) ==  False:
            return []

        final = recursive_sorting(list1, list2)
        
        return final



        

def main():
    solution = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]

    list1_real = full_values(list1)
    list2_real = full_values(list2)
    print(solution.mergeTwoLists(list1_real, list2_real))

    list1 = []
    list2 = []
    list1_real = full_values(list1)
    list2_real = full_values(list2)
    print(solution.mergeTwoLists(list1_real, list2_real))

    list1 = []
    list2 = [0]
    list1_real = full_values(list1)
    list2_real = full_values(list2)
    print(solution.mergeTwoLists(list1_real, list2_real))


    

if __name__ == "__main__":
    main()