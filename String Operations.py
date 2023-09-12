'''
1. Check whether given string is palindrome or not.
2. Find frequency of given char in string.
3. Find the longest length word from the string.
4. Find the frequency of each word from given string.
5. Find the index of first substring
'''


def palindrome():
    str = input("Enter the string: ")
    rev_str = ""
    for i in range(len(str), 0, -1):        #for i in range(initial val, final val, incrmt/decrmnt)
        rev_str = rev_str + str[i-1]        #Here [i-1] is taken because index starts from zero
    print(rev_str)


    if rev_str ==  str:
        print("The string ", str, " is a palindrome.")
    else:
        print("The string ", str, " is not a palindrome.")


print("1. Palindrome\n2. Frequency of given char in string\n3. Longest length word from the string\n"
      "4. Frequency of each word\n5. Index of first substring\n6. Exit")
choice = int(input("Enter the choice: "))

while True:
    if choice == 1:
        palindrome()

    if choice == 6:
        break
