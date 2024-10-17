
def menu():
    C = []
    F = []
    B = []
    
    c_count = int(input("Enter the number of students who play cricket: "))
    f_count = int(input("Enter the number of students who play football: "))
    b_count = int(input("Enter the number of students who play badminton: "))
    
    
    for i in range(c_count):
        c1 = int(input(f"Enter the roll number of student who plays cricket {i + 1}st: "))
        while c1 in C or c1<=0:
            c1 = int(input(f"Please enter a valid and unique roll number for student {i + 1} who plays cricket: "))
        C.append(c1)
        
    
  
    for i in range(f_count):
        f1 = int(input(f"Enter the roll number of student who plays football {i + 1}st: "))
        while f1 in F or f1<=0:
            f1 = int(input(f"Please enter a valid and unique roll number for student {i + 1} who plays football: "))
        F.append(f1)
    
    
    for i in range(b_count):
        b1 = int(input(f"Enter the roll number of student who plays badminton {i + 1}st: "))
        while b1 in B or b1<1:
            b1 = int(input(f"Please enter a valid and unique roll number for student {i + 1} who plays badminton: "))
        B.append(b1)

    
    f = 0
    while f == 0:
        print("\nStudents who play cricket are:", C)
        print("Students who play football are:", F)
        print("Students who play badminton are:", B)
        print("-----------MENU----------")
        print("\n1. List of students who play both cricket and badminton")
        print("2. List of students who play either cricket or badminton but not both")
        print("3. Number of students who play neither cricket nor badminton")
        print("4. Number of students who play cricket and football but not badminton")
        print("5. Quit")
        
        choice = int(input("Choose your option: "))
        while choice < 1 or choice > 5:
            choice = int(input("Invalid choice. Please choose again: "))
        
        if choice == 1:
            print("List of students who play cricket and badminton both :- ",intersection(C,B))
            p = input("Do you want to continue(yes or no)? = ")
            while p!="yes" and p!="no":
                p = input("Please enter answer in yes or no = ")
            if p == "no":
                f = 1
        elif choice == 2:
            print("List of students who play cricket or badminton but not both :- ", diff(union(C,B),intersection(C,B)))
            p = input("Do you want to continue(yes or no)? = ")
            while p!="yes" and p!="no":
                p = input("Please enter answer in yes or no = ")
            if p == "no":
                f = 1
        elif choice == 3:
            print("Number of students who play neither cricket nor badminton :- ",len(diff(diff(F,B),C)))
            p = input("Do you want to continue(yes or no)? = ")
            while p!="yes" and p!="no":
                p = input("Please enter answer in yes or no = ")
            if p == "no":
                f = 1
        elif choice == 4:
            print("Number of students who play cricket and football but not badminton :- ",len(diff(intersection(C,F),B)))
            p = input("Do you want to continue(yes or no)? = ")
            while p != "yes" and p != "no":
                p = input("Please enter answer in yes or no = ")
            if p == "no":
                f=1
        else:
            f = 1
        

def union(a,b):
    union_list = []
    for i in a:
        if i not in union_list:
            union_list.append(i)
        for j in b:
            if j not in union_list:
                union_list.append(j)
    return union_list

def intersection(a,b):
    inter = []
    for i in a:
        for j in b:
            if i == j and i not in inter:
                inter.append(i)
    return inter

def diff(a,b):
    ans = []
    for i in a:
        if i not in b and i not in ans:
            ans.append(i)
    return ans
    

menu()