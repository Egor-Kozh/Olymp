def Main():
    for i in range(1, 10):
        if i < 10:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests3\input_s1_0{i}.txt")
        else:
            file = open(rf"C:\Users\kozhe\OneDrive\Рабочий стол\Tests3\input_s1_{i}.txt")
        text = file.readline().split(" ")
        Text(text)

def Text(text):
    i = int(len(text)/2)
    j = 0
    text2 = ""
    while j != len(text):
        slovo = text[i]
        slovo = Slovo(slovo)
        j = j + 1
        i = i + j*((-1)**j)
        text2 = text2 + slovo + " "
    print(text2)

def Slovo(slovo):
    slovo2 = ""
    i = int(len(slovo) / 2)
    j = 0
    while j != len(slovo):
        letter = slovo[i]
        slovo2 = slovo2 + letter
        j = j + 1
        i = i + j * ((-1) ** j)
    return slovo2


Main()