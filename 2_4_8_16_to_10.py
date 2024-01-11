def fool_check_system(n):
    k = n
    while not (k == '2' or k == '4' or k == '8' or k == '16'):
        print('Please, enter the valid system')
        k = input()
    return int(k)


def fool_check_num(n):
    k = n
    if input_sys != 16:
        while not k.isdigit():
            print('Please, enter the number')
            k = input()
    else:
        flag = True
        for i in k:
            if not i.isdigit() and (i not in letters_16):
                flag = False
        while flag == False:
            print('Please, enter the number')
            k = input()
    return k


def changing_system(n, m):
    for i in input_num:
        n += (int(i) * (m ** input_num.index(i)))
        input_num[input_num.index(i)] = 'a'
    return n

letters_16 = ['A', 'B', 'C', 'D', 'E', 'F']


def changing_system_16(n, m):
    for i in input_num:
        if i.isdigit():
            n += (int(i) * (m ** input_num.index(i)))
            input_num[input_num.index(i)] = 'a'
        else:
            n += ((letters_16.index(i)+10) * (m ** input_num.index(i)))
            input_num[input_num.index(i)] = 'a'

    return n


print('Choose numeric system that you have: 2, 4, 8, 16')
input_sys = fool_check_system(input())
print('Write the number that you want to turn to decimal system:')
input_num = [i for i in fool_check_num(input())]
input_num = input_num[::-1]

output_num = 0

if input_sys == 2:
    print(changing_system(output_num, 2))
elif input_sys == 4:
    print(changing_system(output_num, 4))
elif input_sys == 8:
    print(changing_system(output_num, 8))
elif input_sys == 16:
    print(changing_system_16(output_num, 16))
