x = int(input())
st = ''
for i in range(1, x + 1):
    if x % i == 0:
    	st += (str(i)+" ")
print(st)
