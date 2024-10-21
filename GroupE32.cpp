#include <iostream>
using namespace std;

class PizzaParlor {
    int front, rear, size;
    int* queue;
    
public:
    PizzaParlor(int M) {
        size = M;
        queue = new int[size];
        front = rear = -1;
    }

    bool isFull() {
        return (front == 0 && rear == size - 1) || (rear == (front - 1) % (size - 1));
    }

    bool isEmpty() {
        return front == -1;
    }

    void placeOrder(int orderID) {
        if (isFull()) {
            cout << "Queue is full! Cannot place more orders.\n";
            return;
        }

        if (front == -1) {  
            front = rear = 0;
            queue[rear] = orderID;
        }
        else if (rear == size - 1 && front != 0) {
            rear = 0;  
            queue[rear] = orderID;
        }
        else {
            rear++;
            queue[rear] = orderID;
        }

        cout << "Order " << orderID << " placed successfully.\n";
    }

    void serveOrder() {
        if (isEmpty()) {
            cout << "No orders to serve!\n";
            return;
        }

        cout << "Order " << queue[front] << " served.\n";
        
        if (front == rear) {  
            front = rear = -1;
        }
        else if (front == size - 1) {
            front = 0; 
        }
        else {
            front++;
        }
    }

    
    void displayOrders() {
        if (isEmpty()) {
            cout << "No orders in the queue.\n";
            return;
        }

        cout << "Current orders in the queue: ";
        if (rear >= front) {
            for (int i = front; i <= rear; i++) {
                cout << queue[i] << " ";
            }
        }
        else {
            for (int i = front; i < size; i++) {
                cout << queue[i] << " ";
            }
            for (int i = 0; i <= rear; i++) {
                cout << queue[i] << " ";
            }
        }
        cout << endl;
    }

    ~PizzaParlor() {
        delete[] queue;
    }
};

int main() {
    int M;
    cout << "Enter the maximum number of orders the pizza parlor can accept: ";
    cin >> M;

    PizzaParlor parlor(M);

    int choice, orderID;
    while (true) {
        cout << "\n1. Place Order\n2. Serve Order\n3. Display Orders\n4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter Order ID: ";
                cin >> orderID;
                parlor.placeOrder(orderID);
                break;
            case 2:
                parlor.serveOrder();
                break;
            case 3:
                parlor.displayOrders();
                break;
            case 4:
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}
