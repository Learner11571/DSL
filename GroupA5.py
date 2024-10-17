def menu():
    line = input("\nEnter the line:")
    f = 0
    while f == 0:
        print("\n---------------------MENU---------------------\n")
        print("\n\n1. To display word with the longest length")
        print("2. To determine the frequency of occurrence of a particular character in the string")
        print("3. To check whether the given string is palindrome or not")
        print("4. To display the index of the first appearance of the substring")
        print("5. To count the occurrences of each word in a given string")
        print("6. Quit")

        n = int(input("\nEnter the option number:"))
        while n > 6 or n < 1:
            n = int(input("\nEnter a valid option number:"))

        if n == 1:
            print("\nLongest word in the given string: " + longest_w(line))
        elif n == 2:
            freqofchar(line)
        elif n == 3:
            if palind(line):
                print("\nGiven string is palindrome")
            else:
                print("\nGiven string is not palindrome")
        elif n == 4:
            print("\nFirst occurrence of substring: " + str(idxofsubs(line)))
        elif n == 5:
            occofword(line)
        else:
            break


def longest_w(line):
    max_word = ""
    curr_word = ""
    for i in line + " ":
        if i != " ":
            curr_word += i
        else:
            if len(max_word) < len(curr_word):
                max_word = curr_word
            curr_word = ""
    return max_word


def freqofchar(line):
    ch = input("\nEnter the character to get its frequency: ")
    ch = ch.lower()
    c = 0
    for i in range(len(line)):
        if line[i].lower() == ch:
            c += 1
    print("\nFrequency of " + ch + ": " + str(c))


def palind(line):
    left = 0
    right = len(line) - 1
    while left < right:
        if line[left].lower() != line[right].lower():
            return False
        left += 1
        right -= 1
    return True


def idxofsubs(line):
    subs = input("\nEnter the substring to be found inside the line: ")
    subs = subs.lower()
    idx = -1
    for i in range(len(line)):
        if i + len(subs) <= len(line):
            if line[i:i + len(subs)].lower() == subs:
                idx = i
                break
        else:
            idx = -1
    return idx


def occofword(line):
    line += " "
    L = []
    temp_word = ""
    for i in line:
        if i != " ":
            temp_word += i.lower()
        else:
            if temp_word == " ":
                continue
            L.append(temp_word)
            temp_word = ""
    dict1 = {}
    for i in L:
        if indict(dict1, i):
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(dict1)


def indict(dict1, key1):
    for i in dict1:
        if i == key1:
            return True
    return False


menu()
