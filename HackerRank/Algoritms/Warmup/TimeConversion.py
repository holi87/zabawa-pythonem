#!/bin/python3

import sys, time


timex = input().strip()
zmiana = time.strptime(timex, "%I:%M:%S%p")
zmiana = time.strftime("%H:%M:%S", zmiana)
print(zmiana)
