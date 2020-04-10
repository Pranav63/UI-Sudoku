# w = input()

# l= input()

# af = l.split()
# c=0
# lis=[]

# for i in range(len(af)):
# 	if set(w)==set(af[i]):
# 		lis.append(af[i])
# 	else:
# 		continue


# print (len(set(lis)))

# Board is 9*9 grid with 0 representing an empty space

board= [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7]
]

def printboard(b):
	for i in range(len(b)):
		if i % 3 ==0 and i !=0:
			print("----------------------")

		for j in range(len(b[0])):

			if j % 3 ==0 and j !=0:
				print("|", end=" ")

			if j==8:
				print(b[i][j])
			else:
				print(str(b[i][j])+"", end=" ")



# def valid()  - it requires board , number and postion as input
# we need to check if the postion is valid , we check rows , cols , each square
def valid(b, num, pos):

	#check row - check all elements/columns in a row
	for i in range(len(b[0])):
		# we check for every element of row and also add the constraint that we dont check the current number we added
		if b[pos[0]][i] == num and pos[1] != i:
			return False

		#check column 
	for i in range (len(b)):
		if b[i] [pos[1]] == num and pos[0] != i:
			return False

		#check for each box

	box_X= pos[1]//3
	box_Y= pos[0]//3

	for i in range(box_Y * 3 , box_X*3+3):
		for j in range(box_X*3 , box_Y*3+3):
			if b[i][j] == num and (i,j)!= pos:
				return False 

	return True 



def findempty(b):
	for i in range(len(b)):
		for j in range(len(b[0])):
			if b[i][j]==0:
				return (i,j)
				# print(i,j,end=" ") 
				# row and col

	return None



def backtrack(b):
	soln = findempty(b)
	if not soln:
		return True
	else:
		row, col= soln

	for i in range(1,10):
		if valid(b, i , (row,col)):
			b[row][col]=i 

			if backtrack(b):
				return True 

			b[row][col]=0 

	return False 


print("The given board")
printboard(board)
backtrack(board)
print("===========================")
print ("The solution board")
printboard(board)

