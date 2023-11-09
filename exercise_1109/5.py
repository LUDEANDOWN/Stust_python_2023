def outer_fun(a, b): #回傳相加後再加5 #5
    def sum(a,b):
        return a+b
    sum=sum(a,b)
    return sum+5

result = outer_fun(5, 10)
print(result)

print("\n")