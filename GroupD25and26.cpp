#include <iostream>
#include <string>
using namespace std;

class Stack {
    int top;
    char arr[100];
public:
    Stack() {
        top = -1;
    }
    bool isFull() {
        return top == (sizeof(arr) / sizeof(arr[0])) - 1;
    }
    bool isEmpty() {
        return top == -1;
    }
    void push(char data) {
        if (isFull()) {
            cout << "\nStack is full";
            return;
        }
        arr[++top] = data;
    }
    char pop() {
        if (isEmpty()) {
            cout << "\nStack is empty";
            return '\0';
        }
        return arr[top--];
    }
    char peek() {
        if (isEmpty()) {
            cout << "\nStack is empty";
            return '\0';
        }
        return arr[top];
    }
};

bool isPalin(string str) {
    Stack s;
    for (char ch : str) {
        s.push(ch);
    }
    string reversed;
    int i = 0;
    while (!s.isEmpty()) {
        char ch = s.pop();
        reversed += ch;
        if (ch != str[i++]) {
            return false;
        }
    }
    cout << "Reversed string: " << reversed << endl;  
    return true;
}

bool isWellP(string str) {
    Stack s;
    for (char ch : str) {
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        } else if (ch == ')') {
            if (s.peek() == '(') {
                s.pop();
            } else {
                return false;
            }
        } else if (ch == '}') {
            if (s.peek() == '{') {
                s.pop();
            } else {
                return false;
            }
        } else if (ch == ']') {
            if (s.peek() == '[') {
                s.pop();
            } else {
                return false;
            }
        }
    }
    return s.isEmpty();
}

int main() {
    int choice;
    string str;

    do {
        cout << "\n--- Menu ---\n";
        cout << "1. Check if the string is a palindrome\n";
        cout << "2. Check if the string is well-parenthesized\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter a string: ";
                cin >> str;
                if (isPalin(str)) {
                    cout << "Yes, it's a palindrome.\n";
                } else {
                    cout << "No, it's not a palindrome.\n";
                }
                break;
            case 2:
                cout << "Enter an expression: ";
                cin >> str;
                if (isWellP(str)) {
                    cout << "The expression is well-parenthesized.\n";
                } else {
                    cout << "The expression is not well-parenthesized.\n";
                }
                break;
            case 3:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice, please try again.\n";
        }
    } while (choice != 3);

    return 0;
}
