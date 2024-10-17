def average_score(marks):
    total = 0
    count = 0
    for mark in marks:
        if mark != -1:
            total += mark
            count += 1
    if count == 0:
        return 0
    return total / count

def highest_and_lowest_score(marks):
    highest = None
    lowest = None
    for mark in marks:
        if mark != -1:
            if highest is None or mark > highest:
                highest = mark
            if lowest is None or mark < lowest:
                lowest = mark
    return highest, lowest

def count_absent_students(marks):
    absent_count = 0
    for mark in marks:
        if mark == -1:
            absent_count += 1
    return absent_count

def mark_with_highest_frequency(marks):
    frequency = {}
    for mark in marks:
        if mark != -1:
            if mark not in frequency:
                frequency[mark] = 1
            else:
                frequency[mark] += 1

    highest_freq_mark = None
    highest_freq = 0

    for mark, freq in frequency.items():
        if freq > highest_freq:
            highest_freq = freq
            highest_freq_mark = mark

    return highest_freq_mark

def main():
    n = int(input("Enter the number of students: "))
    marks = []

    for i in range(n):
        while True:
            score = float(input(f"Enter the marks of student {i + 1} (-1 if absent): "))
            if score == -1 or (0 <= score <= 30):
                marks.append(score)
                break
            else:
                print("Invalid input! Please enter a value between 0 and 30 or -1 for absent.")

    while True:
        print("\n--- Menu ---")
        print("1. Calculate Average Score")
        print("2. Find Highest and Lowest Scores")
        print("3. Count Absent Students")
        print("4. Find Mark with Highest Frequency")
        print("5. Exit")
        
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            print(f"Average score of the class: {average_score(marks):.2f}")
        elif choice == 2:
            high, low = highest_and_lowest_score(marks)
            if high is not None and low is not None:
                print(f"Highest score: {high}, Lowest score: {low}")
            else:
                print("No valid scores available.")
        elif choice == 3:
            print(f"Number of absent students: {count_absent_students(marks)}")
        elif choice == 4:
            most_frequent = mark_with_highest_frequency(marks)
            if most_frequent is not None:
                print(f"Mark with highest frequency: {most_frequent}")
            else:
                print("No valid scores to calculate frequency.")
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please choose an option between 1 and 5.")

if __name__ == "__main__":
    main()
