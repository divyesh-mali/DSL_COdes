arr = []

n = int(input("Enter the number of elements: "))

print("Enter the elements in sequential order: ")
for i in range(n):
    elements = int(input(">> "))
    arr.append(elements)

low = 0
high = n-1
mid = (low+high)//2

key = int(input("Enter the element to find: "))

for i in range(n):

    mid = (low + high) // 2

    if arr[mid] == key:
        print("The element ", arr[mid], " is at position ", mid)
        break

    elif arr[mid] < key:
        low = mid + 1
        # print("The element ", arr[mid], " is at position ", mid)

    elif arr[mid] > key:
        high = mid - 1
        # print("The element ", arr[mid], " is at position ", mid)

else:
    print("The element is not present !!")


