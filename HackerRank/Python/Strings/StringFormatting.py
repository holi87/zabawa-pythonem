def print_formatted(number):
    dlugosc = len('{:b}'.format(number))+1
    for i in range(1, number+1):
        print(str.rjust(str(i), dlugosc-1), end = "")
        print(str.rjust('{:o}'.format(i), dlugosc), end = "")
        print(str.rjust('{:X}'.format(i), dlugosc), end = "")
        print(str.rjust('{:b}'.format(i), dlugosc))
