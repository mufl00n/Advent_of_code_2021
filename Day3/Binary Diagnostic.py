with open('sharp.txt') as f:
    lines = f.readlines()
    tmp = [0] * int(len(lines[0])-1)


for number in lines:
    for index, digit in enumerate(number.rstrip()):
        if digit == '1':
            tmp[index] += 1

        else:
            tmp[index] -= 1

gamma = int("".join('0' if x > 0 else '1' for x in tmp),2)
print(gamma)
epsylon = int("".join('0' if x < 0 else '1' for x in tmp),2)
print(epsylon)
print(gamma*epsylon)

