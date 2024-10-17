def binary_search(roll_numbers, target):
    left, right = 0, len(roll_numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if roll_numbers[mid] == target:
            return True
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def fibonacci_search(roll_numbers, target):
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m1 + fib_m2
    while fib_m < len(roll_numbers):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m1 + fib_m2

    offset = -1

    while fib_m > 1:
        index = min(offset + fib_m2, len(roll_numbers) - 1)

        if roll_numbers[index] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = index
        elif roll_numbers[index] > target:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return True

    if fib_m1 and offset + 1 < len(roll_numbers) and roll_numbers[offset + 1] == target:
        return True

    return False

def main():
    n = int(input("Enter the number of students who attended the training program: "))
    roll_numbers = []

    for i in range(n):
        roll_number = int(input(f"Enter roll number of student {i + 1}: "))
        roll_numbers.append(roll_number)

    roll_numbers.sort()

    while True:
        print("\n--- Training Program Attendance ---")
        print("1. Search using Binary Search")
        print("2. Search using Fibonacci Search")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target_roll_number = int(input("Enter the roll number to search: "))
            if binary_search(roll_numbers, target_roll_number):
                print(f"Student with roll number {target_roll_number} attended the training program (Binary Search).")
            else:
                print(f"Student with roll number {target_roll_number} did not attend the training program (Binary Search).")
        
        elif choice == 2:
            target_roll_number = int(input("Enter the roll number to search: "))
            if fibonacci_search(roll_numbers, target_roll_number):
                print(f"Student with roll number {target_roll_number} attended the training program (Fibonacci Search).")
            else:
                print(f"Student with roll number {target_roll_number} did not attend the training program (Fibonacci Search).")
        
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
