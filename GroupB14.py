def selection_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr

def display_top_five_scores(arr):
    sorted_scores_selection = selection_sort(arr.copy())
    print("Top five scores using Selection Sort:")
    for score in sorted_scores_selection[-5:][::-1]:
        print(score)

    sorted_scores_bubble = bubble_sort(arr.copy())
    print("\nTop five scores using Bubble Sort:")
    for score in sorted_scores_bubble[-5:][::-1]:
        print(score)

def main():
    n = int(input("Enter the number of students: "))
    scores = []

    for i in range(n):
        while True:
            score = float(input(f"Enter the percentage of student {i + 1} (0-100): "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid input. Please enter a percentage between 0 and 100.")

    display_top_five_scores(scores)

if __name__ == "__main__":
    main()
