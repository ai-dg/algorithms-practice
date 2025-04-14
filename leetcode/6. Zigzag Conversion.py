class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        map = []

        for x in range(numRows):
            map.append("")

        index = 0
        index_max = numRows - 1
        print(f"str: {s}\nnbr_rows: {numRows}\nindex_max: {index_max}")
        zigzag = False
        
        for c in s:
            map[index] += c
            if index == 0:
                zigzag = False
            elif index == index_max:
                zigzag = True

            if zigzag == True:
                index -= 1 
            else:
                index += 1


        print(map)
        return "".join(map)


def main():
    
    s = "PAYPALISHIRING"
    nbr_rows = 4

    sol = Solution()

    zigzag = sol.convert(s, nbr_rows)
    
    print(f"zigzag: {zigzag}")


if __name__=="__main__":
    main()