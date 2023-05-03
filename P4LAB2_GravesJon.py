''' Type your code here. '''
# get input integer number from user

num1 = int(input())

# get input integer number from user

num2 = int(input())

# check if the value of num1 is less than the value of num2

if(num1 <= num2) :

	# iterating while loop

	while(num1<=num2) :

		# print the value of num1

		print(num1,end=" ")

		# value of num1 is incremented by 5

		num1+=5

	# print and end with a newline

	print()

# otherwise display output

else :

	print("Second integer can't be less than the first.")