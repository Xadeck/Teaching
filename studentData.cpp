#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

class Student
{

public:
    string name;
    string sname;
};

void menu()
{

    cout << "**********************************************************************************" << endl;
    cout << "Choose |1|Enter your data |2|Lessons |3|Averages        (press other key for Exit)" << endl;
    cout << "**********************************************************************************" << endl;
}

// Lessons function
string lessons(vector<string> lessonVector, int &enter_lesson)
{
    cout << "Your lessons are : ";
    for (int i = 0; i < lessonVector.size(); i++)
    {

        cout << i + 1 << "." << lessonVector[i] << " | ";
    }

    cout << "\nChoose your lesson : ";
    cin >> enter_lesson;

    return lessonVector[enter_lesson - 1];
}

// Personal data function
void data(string &personal_data)
{

    cout << "\nWrite things about you here : ";
    getline(cin, personal_data);
}

int main()
{

    Student user;
    int menu_choose;

    // Enter the name
    cout << "Enter your first name : ";
    cin >> user.name;
    cout << "Enter your second name : ";
    cin >> user.sname;

    do
    {
        // Menu
        menu();
        cin >> menu_choose;
        system("cls");

        // Enter personal data
        if (menu_choose == 1)
        {
            string personal_data;
            data(personal_data);

            // Clear the input buffer
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        // Show the lessons and choose one
        if (menu_choose == 2)
        {
            vector<string> lessonVector = {"Math", "English", "Programming", "History"};
            int enter_lesson = 0;
            string choose_lesson = lessons(lessonVector, enter_lesson);

            // Don't allow the user to put a wrong number(lesson)
            if (enter_lesson < 1 || enter_lesson > lessonVector.size())
            {
                cout << "You choosed a wrong lesson\n";
                return 0;
            }
            cout << "You choosed " << choose_lesson << "\n";
        }
    } while (menu_choose > 1 && menu_choose < 4);

    return 0;
}