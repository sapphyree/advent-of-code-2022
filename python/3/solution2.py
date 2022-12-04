

def parse():
    lst = []
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        lst = lines
    return lst

def priority(char):
    # convert to ord, sort priority via range
    o = ord(char)
    if char == char.lower():
        return o - 96
    else:
        return o - 38

def main():
    lst = parse()
    sum = 0
    lst_length = len(lst) // 3
    for i in range(0, len(lst), 3):
        subset = [lst[i], lst[i+1], lst[i+2]]
        intersection = list(set(subset[0]) & set(subset[1]) & set(subset[2]))
        print(intersection)
        p = priority(intersection[0])
        print(p)
        sum += p
    print(sum)


main()