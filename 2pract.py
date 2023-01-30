month31 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
month30 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
month29 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
month28 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

def SumNum (num):
    sum = 0
    j = 1
    for j in num:
        if len(str(num[j])) >= 2:
            numberMass = num[j]
            while (numberMass != 0):
                sum += numberMass % 10
                numberMass = numberMass // 10
        else:
            sum += num[j]
    return sum

year = int(input("Введите год для подсчета числа: "))
while int(year) < 0:
    year = int(input("Введите год больше 0: "))
i = 1
result = 0
for i in range (1,8):
    if i % 2 == 0:
        if i == 2:
            if year % 4 == 0 and (year // 100) % 4 == 0:
                result += SumNum(month29)
            else:
                result += SumNum(month28)
        else:
            result += SumNum(month30)
    else:
        result += SumNum(month31)
    i += 1
for i in range (8, 13):
    if i % 2 == 0:
        result += SumNum(month31)
    else:
        result += SumNum(month30)
    i += 1
print("Сумма: ", result)