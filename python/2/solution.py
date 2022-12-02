# take input, make list?
# parse line, calucate value based on switch case?
# add val of selection, add val of win


def rps(fst, snd):
    sum = 0
    match snd:
        case "X":
            sum += 1
        case "Y":
            sum += 2
        case Z:
            sum += 3

    match fst:
        case "A":
            match snd:
                case "X":
                    sum += 3
                case "Y":
                    sum += 6
                case "Z":
                    sum += 0
        case "B":
            match snd:
                case "X":
                    sum += 0
                case "Y":
                    sum += 3
                case "Z":
                    sum += 6
        case "C":
            match snd:
                case "X":
                    sum += 6
                case "Y":
                    sum += 0
                case "Z":
                    sum += 3
    print(sum)

    return sum

def rps2(fst, snd):
    sum = 0

    match fst:
        case "A":
            match snd:
                case "X": #lose => scissors
                    sum += 3
                case "Y": # draw
                    sum += 4
                case "Z": # win
                    sum += 8
        case "B":
            match snd:
                case "X": # rock 1 + 0
                    sum += 1
                case "Y": # draw => paper 2 + 3
                    sum += 5
                case "Z": # win => scissors 3 + 6
                    sum += 9
        case "C":
            match snd:
                case "X": # lose => paper 2 + 0
                    sum += 2
                case "Y": # draw => scissors 3 + 3
                    sum += 6
                case "Z": # win => rock 1 + 6
                    sum += 7
    print(sum)

    return sum

with open("input.txt") as file:
    lines = [line.rstrip('\n') for line in file]
    sum = 0
    for line in lines:
        x = list(line)
        x.remove(' ')
        sum += rps2(x[0], x[1])
        print(x)
    print(sum)