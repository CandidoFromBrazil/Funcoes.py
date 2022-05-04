def Fibo():
    n1 = 1
    n2 = 0
    sum = 0
    for i in range(10):
        sum = n1 + n2
        n2 = n1
        n1 = sum
        print(sum)
Fibo()