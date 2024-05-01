input_k = 0
while not(input_k > 0 and input_k < 10 and type(input) == int):  # у меня
    # идет преобразование в инт, следовательно, могу не делать проверку на целое число
    input_k = int(input("Введите целове число от 1 до 10 "))

with open('text.txt') as f1:
    lines = f1.readlines()
    if len(lines) == 0:
        print("В файле нет строк")
        quit()

    with open('text2.txt', 'w') as f2:
        if len(lines) < input_k:
            for i in lines:
                f2.write(i)
            quit()
        for i in range(1, input_k + 1):
            f2.write(lines[-i] + '\n')
