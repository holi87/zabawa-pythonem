#Write your code here
# poczatek mojego
class Calculator():
    def power(self, podstawa, wykladnik):
        if podstawa < 0 or wykladnik < 0:
            raise Exception("n and p should be non-negative")
        else:
            return podstawa ** wykladnik
# koniec mojego

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
