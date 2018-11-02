import sys

def fouriermotzkin(A,b,num_var):
	if (len(A) == 0):
		return (A,b)
	m = len(A)
	n = len(A[0])

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

		if(neg > 0):
			position = neg + zer
			for i in range (neg + zer, m):
				c = temp[position]
				temp = [c] + temp
				position += 1
				del temp[position]
		
		for i in range (0, pos + neg):
			ele = float(abs(temp[i][0]))
			if (ele == 0):
				continue
			for j in range (0, len(temp[0])):
				temp[i][j] /= ele 

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
		(A,b) = fouriermotzkin(A,b,num_var);

	elif (n > 0):
		temp = [[0.0 for i in range (0, n)] for j in range (0, len(A))]
		for i in range (0, len(A)):
			for j in range (0, n):
				temp[i][j] = A[i][j]
		A = temp
	return (A,b)

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