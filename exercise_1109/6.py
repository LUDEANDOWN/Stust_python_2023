def sum0toN(sum): #遞迴加總0到N #6
    if sum:
        return sum + sum0toN(sum-1)
    else:
        return 0

print(sum0toN(10))

print("\n")