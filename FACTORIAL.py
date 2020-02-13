#factorial calculator
def fct(n):
    a=n*(n-1)
    if n==1:
        return n
    elif n==0:
        return 0
    else:
        return fct(n-1)*n


num=int(input("number:"))
r=fct(num)
print(r)
