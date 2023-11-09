def keyword(name,age): #打印名子和年齡 #1
    print(name+" and "+str(age))

keyword("Jim",8)

print("\n")

def func1(*number): #打印複數值 #2 
    for i in number:
        print(i)

func1(50,60,70)

print("\n")

def calculation(a, b): #回傳相加和相減 #3
    return a+b,a-b

res = calculation(40, 10)
print(res)

print("\n")

def show_employee(name,salary=9000): #打印薪資,如果沒有就是9000 #4
   print("Name: "+name+" salary: "+str(salary))

show_employee("Ben", 12000)
show_employee("Jessa")

print("\n")

def outer_fun(a, b): #回傳相加後再加5 #5
    return a+b+5

result = outer_fun(5, 10)
print(result)

print("\n")

def sum0toN(sum): #遞迴加總0到N #6
    if sum:
        return sum + sum0toN(sum-1)
    else:
        return 0

print(sum0toN(10))

print("\n")

def display_student(name, age): #7
    print(name, age)

student=display_student#用新名稱呼叫函式 
student("Emma", 26)

print("\n")

def Even_Numbers_N_To_M(N,M): #N~M所有偶數 #8
    for i in range(N,M,2):
        print(i)
Even_Numbers_N_To_M(4,30)


print("\n")

def maxlist(*x): #只打印最大值
    for i in x:
        print(max(i))

x=[1,2,4,8,64,5,8,4,9,12,4]
maxlist(x)