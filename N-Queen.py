# Algorithm
# We rotate the array of initial board - 1,2,4,8,16,......,2^(n-1) => See bit form to visualise the board where 1 shows presence of queen
# 1 => 2,4,8,16,.......,2^(n-1),1	-> initial helper
# 2 => insert 2 in board	then rotate again => 8,16,......1,4
# 3 => insert 8 in board	then rotate again => 32,64,....1,4,16

# Do this for i = 0 to i < (n+1)/2	-> by inspection
# In above code we iterate till (n-1)/2 as 1st case is done separately
from collections import deque
while True:
	while True:
		n = int(input("Enter n for N-Queen (n > 3) : "))
		if n > 3:
			break
		print("n for N-Queen should be greater than 3")

	helper = deque([])
	board = deque([])
	for i in range(n - 1):
		helper.append(2 ** (i + 1))
	helper.append(1)

	for i in range(int((n - 1) / 2)):
		board.append(helper.popleft())
		curr = helper.popleft()
		helper.append(curr)

	while len(helper) > 0:
		curr = helper.popleft()
		board.append(curr)

	while len(board) > 0:
		curr = bin(board.popleft())
		curr = curr[2:]			# Removing 0b from front of bit form
		while len(curr) < n:
			curr = '0' + curr	# Making every bit form of same length
		curr = ' '.join(curr)	# Adding spaces between every bit
		print(curr)
	ans = input("Do you want to continue (y/n) : ")
	if ans != "y" and ans != "Y":
		break



