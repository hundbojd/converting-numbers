def fool_check_system(n):
    k = n
    while not (k == '2' or k == '4' or k == '8' or k == '16'):
        print('Please, enter the valid system')
        k = input()
    return int(k)


def fool_check_num(n):
    k = n
    while not k.isdigit():
        print('Please, enter the number')
        k = input()
    return int(k)


def changing_system(n, m):
    k = input_num
    while k > 0:
        n += str(k % m)
        k = k // m
    return n[::-1]

letters_16 = ['A', 'B', 'C', 'D', 'E', 'F']


def changing_system_16(n, m):
    k = input_num
    while k > 0:
        left = k % m
        if left < 10:
            n += str(left)
        else:
            n += letters_16[left-10]
        k = k // m
    return n[::-1]


print('Choose numeric system that turn your number to: 2, 4, 8, 16')
input_sys = fool_check_system(input())
print('Write the number that you want to turn:')
input_num = fool_check_num(input())


output_num = ''

if input_sys == 2:
    print(changing_system(output_num, 2))
elif input_sys == 4:
    print(changing_system(output_num, 4))
elif input_sys == 8:
    print(changing_system(output_num, 8))
elif input_sys == 16:
    print(changing_system_16(output_num, 16))
