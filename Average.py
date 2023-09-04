marklist = [25, 30, 'a', 21, 23, 30]
def average():
    sum=0
    average=0
    for i in range(len(marklist)):
        if marklist[i] != 'a':
            sum = sum + marklist[i]
            print(sum)
            average = sum // n
            print(average)