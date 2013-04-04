#!/usr/bin/env python3

l = list()
i = 0
while i <= 10 :
    l.append(i)
    i = i + 1
print(l)
l[:] = [12]
print(l)
