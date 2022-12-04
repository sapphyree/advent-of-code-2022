


def priority(char):
    # convert to ord, sort priority via range
    o = ord(char)
    print(o)
    if char == char.lower():
        return o - 96
    else:
        return o - 38

def intersection():
    with open("input.txt", "r") as file:
        lines = [line.rstrip('\n') for line in file]
        sum = 0
        for line in lines:
            comp = int(len(line)) // 2
            left_set = set(line[:comp])
            #print(left_set)
            right_set = set(line[comp:])
            #print(right_set)
            intersection = list(left_set.intersection(right_set))
            print(intersection)
            p = priority(intersection[0])
            sum += p
        print(sum)

intersection()