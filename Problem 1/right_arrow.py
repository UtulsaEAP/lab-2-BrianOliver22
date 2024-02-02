def right_arrow():
    base_char = input("write base characer here")
    head_char = input("write base character here")

    row1 = '      ' + head_char
    row2 = '      ' + head_char + head_char
    row3 = '      ' + head_char + head_char + head_char
    ''' Type your code here. '''

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()