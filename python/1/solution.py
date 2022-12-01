#f = open("input.txt", "r")

elf_list = []
i = 0
sum = 0
lst = []

with open("input.txt") as file:
    lines = [line.rstrip('\n') for line in file]
    for line in lines:
        #print(line)
        if line == "":
            #print(sum)
            lst.append(sum)
            sum = 0
        else:
            sum += int(line)
            if (lines.index(line) == len(lines) - 1):
                lst.append(sum)

print(max(lst))
lst.sort(reverse=True)

top3 = 0

for i in range(0,3):
    top3 += lst[i]

print(top3)