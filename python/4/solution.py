import re

def parse():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

def createArray(start, end):
    arr = []
    for i in range(int(start),int(end)+1):
        arr.append(i)
    print(arr)
    return arr

def main():
    lst = parse()
    subsetCount = 0

    for elem in lst:
        ids = re.split(r'[-,]', elem)
        a1 = createArray(ids[0],ids[1])
        a2 = createArray(ids[2], ids[3])
        if not (set(a1).isdisjoint(set(a2))):
            print("a2 contains a1")
            subsetCount +=1
        elif not (set(a2).isdisjoint(set(a1))):
            print("a1 contains a2")
            subsetCount += 1
        else:
            print("no subset :(")

    print(subsetCount)

main()