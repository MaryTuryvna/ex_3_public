x = 0
number_sequence = []    #список введених чисел
while x <= 3:
    print("Введіть послідовність чисел ")
    number = int(input(''))
    number_sequence.append(number)
    x += 1
number_sequence.sort()
print(number_sequence)    #відсортований список чисел
