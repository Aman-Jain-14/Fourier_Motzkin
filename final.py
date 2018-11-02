import sys

def fouriermotzkin(A,b,num_var):
	if (len(A) == 0):
		return (A,b)
	m = len(A)
	n = len(A[0])

	# print 'A here = '
	# print A
	# print 'b = here '
	# print b
	neg = pos = zer = 0
	if (n > num_var):
		temp = [[0 for i in range (0, n+1)] for j in range (0, m)]
		for i in range (0, m):
			for j in range (0, n):
				temp[i][j] = A[i][j]
			temp[i][n] = b[i]

		temp = sorted(temp,key=lambda temp: temp[0])
		for i in range (0, m):
			if(temp[i][0] < 0):
				neg += 1
			elif (temp[i][0] == 0):
				zer += 1
			else:
				pos += 1

		# print 'sorted temp = '
		# print temp

		if(neg > 0):
			position = neg + zer
			for i in range (neg + zer, m):
				# print ' i = '
				# print i

				c = temp[position]
				# print 'c = ',c
				temp = [c] + temp
				position += 1
				# print 'len = ',len(temp)
				# print 'position = ',position
				del temp[position]
				# print 'temp now = ',
				# print temp
			# for i in range (m, m + pos):
			# 	del temp[-1]

		# print 'neg = ',neg,' pos = ',pos,' zer = ',zer
		# print 'Arranged temp = '
		# print temp
		
		# print 'len here = ',len(temp)
		# print 'pos + neg = ',pos+neg
		for i in range (0, pos + neg):
			ele = float(abs(temp[i][0]))
			if (ele == 0):
				continue
			for j in range (0, len(temp[0])):
				temp[i][j] /= ele 

		# print 'normalized temp = '
		# print temp
		if (neg == 0):
			A = [[0.0 for i in range (0,n)] for j in range (0,((pos*(pos+1)/2)-pos) + zer)]
			count = 0
			for i in range (0, pos):
				for j in range (i+1, pos):
					for k in range (0, n):
						A[count][k] = temp[i][k+1] - temp[j][k+1]
					count += 1
		else:
			A = [[0.0 for i in range (0, n)] for j in range(0, pos*neg+zer)]
			count = 0
			for i in range (0, pos):
				for j in range (pos, pos+neg):
					for k in range (1, n+1):
						A[count][k-1] = temp[i][k] + temp[j][k]
					count += 1

		position = pos + neg
		for i in range (pos*neg, pos*neg+zer):
			for j in range (1, n+1):
				A[i][j-1] = temp[position][j]
			position += 1

		b = [0.0 for j in range (0, len(A))]
		for i in range (0, len(A)):
			b[i] = A[i][n-1]

		temp = [[0.0 for i in range (0, n-1)] for j in range (0, len(A))]
		for i in range (0, len(A)):
			for j in range (0, n-1):
				temp[i][j] = A[i][j]
		
		A = temp

		# print 'A = '
		# print A
		# print 'b = '
		# print b
		(A,b) = fouriermotzkin(A,b,num_var);

	elif (n > 0):
		temp = [[0.0 for i in range (0, n)] for j in range (0, len(A))]
		for i in range (0, len(A)):
			for j in range (0, n):
				temp[i][j] = A[i][j]
		A = temp
	return (A,b)

print 'Enter dimensions of matrix A:'
n = int(raw_input())
a = [[0.0 for i in range (0,int(n))] for j in range (0,int(n))]
print 'Enter elements of A (one row at a time):'
for i in range (0, int(n)):
	a[i] = [float(x) for x in sys.stdin.readline().split()]
b = [[0.0 for i in range (1)] for j in range (int(n))]
print 'Enter elements of b (b1 b2 b3 . . . bn):'
b = [float(x) for x in sys.stdin.readline().split()]
# print a
# print b

print '\n Figure ',sys.maxint,' means +ve infinity and ',-1*sys.maxint-1,' means -ve infinity'
print '\nSolutions : '

up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'

flag = 0
for i in range (0, n):
	if(up_var[i] == sys.maxint or low_var[i]== -1*sys.maxint -1):
		flag = 1
		break

if (flag == 1):
	print ' This set of inequalities has infinite solutions [check the bounds to confirm]\n'
else:
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
	print sol_mat

a = [[0 for i in range (0,3)] for j in range (0,3)]
b = [[0 for i in range (0,1)] for j in range (0,3)]

a[0][0] = -1
a[0][1] = -1
a[0][2] = 2

a[1][0] = 1
a[1][1] = 3
a[1][2] = -1

a[2][0] = 0
a[2][1] = -1
a[2][2] = -1

b[0] = -2
b[1] = 0
b[2] = -1

# (X,Y) = fouriermotzkin(a,b,0)
# print X
# print Y
# up_var = []
# up_var.insert(0,1.0/X[0][0] * Y[0])
# for i in range (2, len(a[0])+1):
# 	(A,B) = fouriermotzkin(a,b,i)
# 	l = []
# 	diff = 0
# 	for j in range (1, i):
# 		diff += A[0][j]*up_var[j-1]
# 	up_var.insert(0,((B[0] - diff)/A[0][0]))
# # print 'Upper bound = '
# print up_var


# print 'a = '
# print a
up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'

a = [[0 for i in range (0,3)] for j in range (0,3)]
b = [[0 for i in range (0,1)] for j in range (0,3)]
a[0][0] = -1
a[0][1] = 5
a[0][2] = 2

a[1][0] = -3
a[1][1] = 2
a[1][2] = 6

a[2][0] = 2
a[2][1] = -5
a[2][2] = 4

b[0] = -7
b[1] = 12
b[2] = 10

up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'

a = [[0 for i in range (0, 2)] for j in range (0,2)]
b = [[0 for i in range (0, 1)] for j in range (0,2)]
a[0][0] = 5 
a[0][1] = 3
a[1][0] = 2
a[1][1] = 5

b[0] = 8
b[1] = 15


up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'

# a = [[0.0 for i in range (0, 2)] for j in range (0,2)]
# b = [[0.0 for i in range (0, 1)] for j in range (0,2)]
# a[0][0] = 1
# a[0][1] = -1
# a[1][0] = -1
# a[1][1] = 1

# b[0] = -2
# b[1] = -2

# (X,Y) = fouriermotzkin(a,b,1)
# if(X[0][0] == 0):
# 	print 'X = '
# 	print X
# 	print 'y = '
# 	print Y
# 	print 'No Solution'
# else:
# 	print X
# 	print Y

a = [[0 for i in range (0,2)] for j in range (0,2)]
b = [[0 for i in range (0,1)] for j in range (0,2)]
a[0][0] = -3
a[0][1] = 2
# a[0][2] = 0

a[1][0] = 2
a[1][1] = -3
# a[1][2] = 0

# a[2][0] = 0
# a[2][1] = 1
# a[2][2] = 0

b[0] = 0
b[1] = 1
# b[2] = 2

up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'

a = [[0 for i in range (0, 3)] for j in range (0,3)]
b = [[0 for i in range (0, 1)] for j in range (0,3)]
a[0][0] = 0
a[0][1] = 5
a[0][2] = -7

a[1][0] = 4
a[1][1] = -8
a[1][2] = 0

a[2][0] = -4 
a[2][1] = 0
a[2][2] = 1

b[0] = 99
b[1] = 0
b[2] = 0

up_var = [sys.maxint for i in range (len(a[0]))]
low_var = [-1*sys.maxint -1 for i in range (len(a[0]))]
n = len(a[0]) - 1
for j in range (0, len(a[0])):
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if(X[0][0] < 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	elif(X[0][0] > 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]

for i in range (0, len(a)):
	for j in range (0, len(a[0])):
		a[i][j] *= -1
for i in range (0, len(b)):
	b[i] *= -1

n = len(a[0]) - 1
for j in range (0, len(a[0])):	
	(X,Y) = fouriermotzkin(a,b,1)
	if (len(X) == 0):
		continue
	if (X[0][0] < 0):
		up_var[n-j] = 1.0/X[0][0] * Y[0]
	elif (X[0][0] > 0):
		low_var[n-j] = 1.0/X[0][0] * Y[0]
	for i in range (0, len(a)):
		a[i].insert(0, a[i][len(a[0])-1])
		del a[i][-1]
print 'Upper bounds = '
print up_var
print 'Lower bounds = '
print low_var
print '\n'