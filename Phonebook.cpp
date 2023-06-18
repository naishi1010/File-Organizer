#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// Node structure for the B+ tree
struct Node {
    vector<string> keys;
    vector<Node*> children;
    bool isLeaf;
};

// Phonebook class
class Phonebook {
private:
    Node* root;
    fstream file;

public:
    Phonebook(const string& filename) : root(nullptr), file(filename, ios::out | ios::in | ios::app) {}

    ~Phonebook() {
        file.close();
    }

    void insertContact(const string& name, const string& phoneNumber, const string& address) {
        // Insert the contact into the B+ tree structure in memory

        // Write the contact to the file
        file << name << "|" << phoneNumber << "|" << address << endl;
    }

    bool searchContact(const string& contact) {
        file.seekg(0, ios::beg); // Reset file pointer to the beginning
        string line;
        while (getline(file, line)) {
            size_t delimiterPos = line.find("|");
            string name = line.substr(0, delimiterPos);
            if (name == contact) {
                string phoneNumber = line.substr(delimiterPos + 1, line.find("|", delimiterPos + 1) - delimiterPos - 1);
                string address = line.substr(line.find_last_of("|") + 1);
                
                cout << "Contact Details:" << endl;
                cout << "Name: " << name << endl;
                cout << "Phone Number: " << phoneNumber << endl;
                cout << "Address: " << address << endl;
                
                return true;
            }
        }
        return false;
    }

};

int main() {
    Phonebook phonebook("phonebook.txt");

    int choice;
    string name, phoneNumber, address;

    while (true) {
        cout << "Phonebook Application" << endl;
        cout << "1. Add Contact" << endl;
        cout << "2. Search Contact" << endl;
        cout << "3. Quit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter contact details:" << endl;
                cout << "Name: ";
                cin.ignore();
                getline(cin, name);
                cout << "Phone Number: ";
                getline(cin, phoneNumber);
                cout << "Address: ";
                getline(cin, address);
                phonebook.insertContact(name, phoneNumber, address);
                cout << "Contact added successfully!" << endl;
                break;

            case 2:
                cout << "Enter contact name to search: ";
                cin.ignore();
                getline(cin, name);
                if (phonebook.searchContact(name)) {
                    cout << "Contact found!" << endl;
                } else {
                    cout << "Contact not found." << endl;
                }
                break;

            case 3:
                cout << "Exiting Phonebook Application." << endl;
                return 0;

            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }

        cout << endl;
    }
}
