def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target:
            return True
    return False

def sentinel_search(roll_numbers, target):
    n = len(roll_numbers)
    last = roll_numbers[n - 1]
    roll_numbers[n - 1] = target
    
    i = 0
    while roll_numbers[i] != target:
        i += 1
    
    roll_numbers[n - 1] = last
    
    return i < n - 1

def main():
    n = int(input("Enter the number of students who attended the training program: "))
    roll_numbers = []

    for i in range(n):
        roll_number = int(input(f"Enter roll number of student {i + 1}: "))
        roll_numbers.append(roll_number)

    while True:
        print("\n--- Training Program Attendance ---")
        print("1. Search using Linear Search")
        print("2. Search using Sentinel Search")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target_roll_number = int(input("Enter the roll number to search: "))
            if linear_search(roll_numbers, target_roll_number):
                print(f"Student with roll number {target_roll_number} attended the training program (Linear Search).")
            else:
                print(f"Student with roll number {target_roll_number} did not attend the training program (Linear Search).")
        
        elif choice == 2:
            target_roll_number = int(input("Enter the roll number to search: "))
            if sentinel_search(roll_numbers, target_roll_number):
                print(f"Student with roll number {target_roll_number} attended the training program (Sentinel Search).")
            else:
                print(f"Student with roll number {target_roll_number} did not attend the training program (Sentinel Search).")
        
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
