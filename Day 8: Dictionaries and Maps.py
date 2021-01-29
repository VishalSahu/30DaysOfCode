# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
if (1<=n<=100000):
    d = {}
    for i in range(n):
        keys,values = input().split() 
        d[keys] = values
    for i in range(n):
        try:
            ser = input()
            if ser in d:
                print(ser+"="+d[ser])
            else:
                print("Not found")
        except:
            break
