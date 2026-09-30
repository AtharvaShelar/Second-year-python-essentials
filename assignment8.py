def calculate_area(shape, x, y = 0):
	if shape == "circle":
		return 3.14 * x * x;
	elif shape == "rectangle":
		return x * y
	elif shape == "triangle":
		return 0.5 * x * y;
while True:
	shape = input("Enter shape (circle/rectangle/triangle) or exit :")
	if shape == "circle":
		r = float(input("Enter radius of the circle: "));
		print("area is", calculate_area(shape, r))
	if shape == "rectangle":
		l = float(input("Enter the length of the rectangle: "))
		b = float(input("Enter the breadth of the rectangle: "))
		print("Area is :", calculate_area(shape, l, b))
	if shape == "triangle":
		b = float(input("Enter base of the triangle: "))
		h = float(input("Enter height of the triangle: "))
		print("Area is: ", calculate_area(shape,b,h))
	
	if shape == "exit":
		print("Program ended")
		break

