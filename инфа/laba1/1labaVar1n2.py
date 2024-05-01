lis = list()
with open('lab1_N2_txt.txt', "r") as f:
    with open('lab1_N2.txt', 'w') as f2:
        for sym in f.readlines():
            for i in sym:
                if i not in lis:
                    lis.append(i)
        for i in lis:
            f2.write(i)
