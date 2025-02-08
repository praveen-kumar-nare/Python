
def power(N, P):

	
	if P == 0:
		return 1


	if P%2 == 0:
	result = power(N, P//2)
	return result * result
	else :
	result = power(N, (P-1)//2)
	return N * result * result 



if __name__ == '__main__':
	N = 5
	P = 2

	print(power(N, P))
