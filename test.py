import sys

a = [[0 for i in range (0,5)] for j in range (0,4)]
# print a
n = len(a[0])
m = len(a)

a[0][0] = 5
a[0][1] = 7
a[0][2] = 1
a[0][3] = 9
a[0][4] = 3

a[1][0] = 2
a[1][1] = 2
a[1][2] = 9
a[1][3] = 1
a[1][4] = 5

a[2][0] = -1
a[2][1] = 4
a[2][2] = 2
a[2][3] = 7
a[2][4] = 9

a[3][0] = 3
a[3][1] = 1
a[3][2] = 8
a[3][3] = 6
a[3][4] = 5

# print a
a = sorted(a,key=lambda a: a[0])
# print a

b = [0 for i in range (0, len (a[0]))]
b.append(a[3])
c = a[3]
a = [c] + a
# print a 
del a[-1]
# print a

# for i in range (0, len(a)):
# 	for j in range (0, len(a[0])):
# 		a[i].append(a[i][j])
# print a

# for i in range (0, m):
# 	if(a[i][0] == 0 or a[i][0] == 1 or a[i][0] == -1):
# 		continue
# 	else:
# 		div = float(a[i][0])
# 		for j in range (0, n):
# 			a[i][j] /= div
# print a
# print 'Enter dimensions of matrix A:'
# n = raw_input()
# a = [[0.0 for i in range (0,int(n))] for j in range (0,int(n))]
# print 'Enter elements of A (one row at a time):'
# for i in range (0, int(n)):
# 	a[i] = [float(x) for x in sys.stdin.readline().split()]
# b = [[0.0 for i in range (1)] for j in range (int(n))]
# print 'Enter elements of b (b1 b2 b3 . . . bn):'
# b = [float(x) for x in sys.stdin.readline().split()]
# print a
# print b

up = []
low = []
up.append(4)
up.append(3)
up.append(5)

low.append(-4)
low.append(-4)
low.append(-1)

sol_space = 1
for i in range (0 , len(up)):
	temp = up[i] - (low[i]-1)
	sol_space *= temp
print sol_space

sol_mat = [[0 for i in range (0,len(up))] for j in range (0,sol_space)]
times = 1
for i in range (len(up)-1, -1, -1):
	print 'i = ',i
	count = 0
	element = low[i]
	while(count < sol_space):
		for j in range (0, times):
			sol_mat[count][i] = element
			count += 1
			if(count >= sol_space):
				break
		element += 1
		if(element > up[i]):
			element = low[i]
	times *= up[i] - (low[i]-1)
# sol_mat.sort()
print sol_mat