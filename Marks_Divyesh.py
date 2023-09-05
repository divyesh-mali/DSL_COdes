def average(n):
    sum=0
    avg=0
    for i in range(n):
        if marklist[i] != 'A':
            sum = sum + int(marklist[i])
    print(sum)
    average = sum // n
    print("The average of marks is: ", average)

def absent():
    choice = 0
    for i in range(len(marklist)):
        if marklist[i]=='A':
            choice+=1
    print("Total number of absent students: ", choice)


def highest_marks():
    highest = marklist[0]
    if marklist[0] == 'A':
        highest = marklist[1]
        for i in range(len(marklist)):
            if int(marklist[i] == 'A'):
                continue
                if int(highest) < int(marklist[i]):
                    highest = int(marklist[i])

    elif marklist[0] != 'A':
        for i in range(len(marklist)):
            if int(marklist[i] == 'A'):
                continue
                if int(highest) < int(marklist[i]):
                    highest = int(marklist[i])
            elif int(highest) < int(marklist[i]):
                highest = int(marklist[i])
        print("The highest marks is: ", highest)



def lowest_marks():
    lowest = marklist[0]
    if marklist[0] == 'A':
        lowest = marklist[1]
        for i in range(len(marklist)):
            if int(marklist[i] == 'A'):
                continue
                if int(lowest) > int(marklist[i]):
                    lowest = int(marklist[i])

    elif marklist[0] != 'A':
        for i in range(len(marklist)):
            if int(marklist[i] == 'A'):
                continue
                if int(lowest) > int(marklist[i]):
                    lowest = int(marklist[i])
            elif int(lowest) > int(marklist[i]):
                lowest = int(marklist[i])

        print("The lowest marks is: ", lowest)


marklist=[]
n = int(input("Enter number of students: "))

print("Enter marks of students. Enter 'A' if student is absent.")

for i in range(n):
    marks=input("Enter marks: ")
    marklist.append(marks)
print(marklist)

while True:
    print("1. Average\n 2. Count of absent students\n 3. Lowest marks\n 4. Highest marks\n"
          "5. Marks with highest frequency\n 6. Exit\n")

    choice = int(input("Enter the choice: "))

    if choice==1:
        average(n)

    elif choice==2:
        absent()

    elif choice==3:
        lowest_marks()

    elif choice==4:
        highest_marks()



