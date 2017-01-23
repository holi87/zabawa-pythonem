n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr = list(reversed(arr))
# for i in range(n-1):
#     print("%d " % arr[i], end="")
# print(arr[n-1], end="")


# How to make it in hard way :D

print(" ".join(map(str, arr)))