#program to take a string as input from the user and then #check if it contains any hidden message or not

mes = input("Enter the string that might contain the hidden message: ")
a = input("Enter the hidden message you want to check in the message: ")
if a in mes:
	print("Secret message found!")
else:
	print("No secret message found!") 