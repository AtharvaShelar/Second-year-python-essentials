# assignment 5
n = int(input("Enter number of students: "))
total = 0

for i in range(n):
    sum = 0
    print("Student", i + 1)

    for j in range(5):
        score = float(input("Enter test score: "))
        sum += score

    avg = sum / 5
    total += sum
    print("Average =", avg)

print("Overall average =", total / (n * 5))
