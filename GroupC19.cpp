#include <iostream>
#include <string>

using namespace std;

struct Member {
    string prn;
    string name;
    Member* next;
};

class Club {
private:
    Member* head;

public:
    Club() : head(nullptr) {}

    void addMember(const string& prn, const string& name) {
        Member* newMember = new Member{prn, name, nullptr};
        if (!head) {
            head = newMember;
        } else {
            Member* temp = head;
            while (temp->next) {
                temp = temp->next;
            }
            temp->next = newMember;
        }
    }

    void deleteMember(const string& prn) {
        if (!head) {
            cout << "Club is empty, no members to delete.\n";
            return;
        }

        if (head->prn == prn) {
            Member* temp = head;
            head = head->next;
            delete temp;
            cout << "President removed successfully.\n";
            return;
        }

        Member* current = head;
        Member* previous = nullptr;

        while (current && current->prn != prn) {
            previous = current;
            current = current->next;
        }

        if (!current) {
            cout << "Member not found.\n";
            return;
        }

        previous->next = current->next;
        delete current;
        cout << "Member removed successfully.\n";
    }

    int totalMembers() const {
        int count = 0;
        Member* temp = head;
        while (temp) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    void displayMembers() const {
        if (!head) {
            cout << "No members in the club.\n";
            return;
        }

        cout << "Members of the Pinnacle Club:\n";
        Member* temp = head;
        while (temp) {
            cout << "PRN: " << temp->prn << ", Name: " << temp->name << endl;
            temp = temp->next;
        }
    }

    void concatenate(Club& other) {
        if (!head) {
            head = other.head;
        } else {
            Member* temp = head;
            while (temp->next) {
                temp = temp->next;
            }
            temp->next = other.head;
        }
    }
};

int main() {
    Club divisionA, divisionB;
    int choice;
    string prn, name;

    do {
        cout << "\n--- Pinnacle Club Management ---\n";
        cout << "1. Add Member to Division A\n";
        cout << "2. Add Member to Division B\n";
        cout << "3. Delete Member from Division A\n";
        cout << "4. Delete Member from Division B\n";
        cout << "5. Display Members of Division A\n";
        cout << "6. Display Members of Division B\n";
        cout << "7. Compute Total Members in Division A\n";
        cout << "8. Compute Total Members in Division B\n";
        cout << "9. Concatenate Division B to Division A\n";
        cout << "10. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter PRN: ";
                cin >> prn;
                cout << "Enter Name: ";
                cin.ignore();
                getline(cin, name);
                divisionA.addMember(prn, name);
                break;
            case 2:
                cout << "Enter PRN: ";
                cin >> prn;
                cout << "Enter Name: ";
                cin.ignore();
                getline(cin, name);
                divisionB.addMember(prn, name);
                break;
            case 3:
                cout << "Enter PRN of member to delete: ";
                cin >> prn;
                divisionA.deleteMember(prn);
                break;
            case 4:
                cout << "Enter PRN of member to delete: ";
                cin >> prn;
                divisionB.deleteMember(prn);
                break;
            case 5:
                divisionA.displayMembers();
                break;
            case 6:
                divisionB.displayMembers();
                break;
            case 7:
                cout << "Total members in Division A: " << divisionA.totalMembers() << endl;
                break;
            case 8:
                cout << "Total members in Division B: " << divisionB.totalMembers() << endl;
                break;
            case 9:
                divisionA.concatenate(divisionB);
                cout << "Division B members concatenated to Division A.\n";
                break;
            case 10:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice, please try again.\n";
        }
    } while (choice != 10);

    return 0;
}
