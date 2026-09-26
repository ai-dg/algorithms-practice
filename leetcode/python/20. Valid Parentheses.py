class Solution(object):

    def count_number(self, s : str):
        if s.count("{") != s.count("}"):
            return False
        if s.count("(") != s.count(")"):
            return False
        if s.count("[") != s.count("]"):
            return False

        return True
        

    def isValid(self, s : str):
        """
        :type s: str
        :rtype: bool
        """
        PARENTHESES_LIST = ["(", ")", "{", "}", "[", "]"]

        if len(s) <= 1 or len(s) > 10**4:
            return False

        if any(char not in PARENTHESES_LIST for char in s):
            return False

        if self.count_number(s) == False:
            return False

        stack = []
        for i, value in enumerate(s):
            if value == "(" or value == "[" or value == "{":
                stack.append(value)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if value == ")" and top != "(":
                    return False
                if value == "]" and top != "[":
                    return False
                if value == "}" and top != "{":
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        
        




def main():
    solution = Solution()
    s = "a()"
    print("Example #1")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")
    s = "()"
    print("Example #2")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")
    s = "()[]{}"
    print("Example #3")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")
    s = "(]"
    print("Example #4")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")
    s = "([])"
    print("Example #5")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")
    s = "([)]"
    print("Example #6")
    print(f"Test: {s} \nSolution: {solution.isValid(s)}")


    




if __name__ == "__main__":
    main()