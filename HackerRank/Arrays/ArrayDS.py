n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr = list(reversed(arr))
print(" ".join(map(str, arr)))
