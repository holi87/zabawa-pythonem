T = int(input())
dzielenie = []
for i in range(T):
    dzielenie.append(input().split())
# sprawdzmy poprawnosc danych
# print(T)
# print(dzielenie)
for j in range(T):
    # for k in range(2):
    try:
        print(int(dzielenie[j][0]) // int(dzielenie[j][1]))
    except Exception as e:
        print("Error Code:",e)
    #except ValueError as v:
    #    print ("Error Code:", v)
    #except ZeroDivisionError as z:
    #    print("Error Code:", z)