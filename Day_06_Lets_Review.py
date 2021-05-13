r=int(input())
while r>0:
    s = input()
    s1=""
    s2=""
    length = len(s)
    for i in range(length):
        if i%2==0:
            s1 = s1 + s[i]
        else:
            s2 = s2 + s[i]
    print(s1+" "+s2)
    r=r-1
