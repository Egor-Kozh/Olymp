def Main():
    for i in range(1, 21):
        if i < 10:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests4\input_s1_0{i}.txt")
        else:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests4\input_s1_{i}.txt")
        n = int(file.readline())
        slova = []
        for _ in range(n):
            slova.append(file.readline())

        n = int(file.readline())
        upblock = [[],[]]
        for _ in range(n):
            cash = file.readline().split(" ")
            upblock[0].append(cash[0])
            upblock[1].append(int(cash[1]))

        n = int(file.readline())
        downblock = [[], []]
        for _ in range(n):
            cash = file.readline().split(" ")
            downblock[0].append(cash[0])
            downblock[1].append(int(cash[1]))

        Gold_Fish(slova, upblock, downblock)

def Gold_Fish(slova, upblock, downblock):
    result = 0
    a = max(upblock[1])
    for j in range(a):
        for i in range(len(slova)):
            slovo = slova[i]
            chek1, a = check_up(slovo, upblock)
            chek2, b = check_down(slovo, downblock)
            if j == 0 and (chek1 and chek2) and (upblock[1][a] != 0 and downblock[1][b] != 0) and (upblock[0][a] == downblock[0][b]):
                result = result + 1
                upblock[1][a] = upblock[1][a] - 1
                downblock[1][b] = downblock[1][b] - 1
                slova[i] = "   "
            elif (chek1 and chek2) and (upblock[1][a] != 0 and downblock[1][b] != 0) and (upblock[1][a] == max(upblock[1]) and downblock[1][b]==max(downblock[1])):
                result = result + 1
                upblock[1][a] = upblock[1][a] - 1
                downblock[1][b] = downblock[1][b] - 1
                slova[i] = "   "

    print(result)

def check_up(slovo, upblock):
    letter = slovo[0]
    a = 0
    chek = False
    for i in range(len(upblock[0])):
        if letter == upblock[0][i]:
            a = i
            chek = True
    return chek, a

def check_down(slovo, downblock):
    letter = slovo[-2]
    b = 0
    chek = False
    for i in range(len(downblock[0])):
        if letter == downblock[0][i]:
            b = i
            chek = True
    return chek, b

Main()