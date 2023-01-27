import sys
d = "100"
while d != "0":
    d = input()
    dd = len(d) // 2
    c = 1
    for i in range(dd):
        if d[i] != d[len(d)-(i+1)]:
            print("no")
            c = 0
            break
    if c == 1:
        print("yes")
