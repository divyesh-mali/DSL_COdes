def average(n):
    sum=0
    avg=0
    for i in range(n):
        if marklist[i] != 'A':
            sum = sum + int(marklist[i])
        print(sum)
        average = sum // n
        print("The average of marks is: ", average)

marklist=[]
n = int(input("Enter number of students: "))

print("Enter marks of students. Enter 'A' if student is absent.")

for i in range(n):
    marks=input("Enter marks: ")
    marklist.append(marks)
print(marklist)

while True:
    print("1. Average\n 2. Count of absent students\n 3. Lowest & highest marks\n"
          "4. Marks with highest frequency\n")

    ch = int(input("Enter the choice: "))

    if ch==1:
        average(n)
