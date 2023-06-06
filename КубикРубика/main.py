def Main():
    for i in range(1, 21):
        if i < 10:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests\input_s1_0{i}.txt")
        else:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests\input_s1_{i}.txt")
        a = file.readline().split(" ")
        n = int(a[0]);
        m = int(a[1])
        a = file.readline().split(" ")
        x = int(a[0]);
        y = int(a[1]);
        z = int(a[2])
        switchPoint(n, m, x, y, z, file)

def switchPoint(n, m, x, y, z, file):
    for i in range(m):
        aks = file.readline().split(" ")
        a = str(aks[0]); k = int(aks[1]); s = int(aks[2])
        if a == "X":
            if k == x:
                y, z = VrashenieBlock(s, n, y, z)
        if a == "Y":
            if k == y:
                x, z = VrashenieBlock(s, n, x, z)
        if a == "Z":
            if k == z:
                x, y = VrashenieBlock(s, n, x, y)
    print(x,y,z)

def VrashenieBlock(s, n, a, b):
    if s == 1:
        q = a
        a = b
        b = n + 1 - q
        return a, b
    else:
        q = b
        b = a
        a = n + 1 - q
        return a, b

Main()
