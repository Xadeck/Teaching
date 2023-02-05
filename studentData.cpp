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

    cout << "*******************************************************************************************" << endl;
    cout << "Choose |1|Enter your data |2|Lessons |3|Averages and Data        (press other key for Exit)" << endl;
    cout << "*******************************************************************************************" << endl;
}

// Lessons function
string lessons(vector<string> lessonVector, int &enter_lesson, vector<int> math, vector<int> english,
               vector<int> programming, vector<int> history)
{
    cout << "Your lessons are : ";
    for (int i = 0; i < lessonVector.size(); i++)
    {

        cout << i + 1 << "." << lessonVector[i] << " | ";
    }

    cout << "\nChoose your lesson : ";
    cin >> enter_lesson;

    // Don't allow the user to put a wrong number(lesson)
    if (enter_lesson < 1 || enter_lesson > lessonVector.size())
    {
        cout << "You chose a wrong lesson.\n";
        return "";
    }

    return lessonVector[enter_lesson - 1];
}

// Personal data function
void data(string &personal_data)
{

    cout << "\nWrite things about you here : ";
    getline(cin, personal_data);
}

// Average function
void average(int avmath, int avenglish, int avprogramming, int avhistory, vector<int> math, vector<int> english,
            vector<int> programming, vector<int> history)
{
    avmath /= math.size();
    avenglish /= english.size();
    avprogramming /= programming.size();
    avhistory /= history.size();

}

int main()
{

    Student user;
    int menu_choose;
    string personal_data;
    vector<string> lessonVector = {"Math", "English", "Programming", "History"};
    vector<int> math;
    vector<int> english;
    vector<int> programming;
    vector<int> history;
    int enter_lesson = 0;
    int num_of_grades;
    int grade;
    int avmath = 0, avenglish = 0, avprogramming = 0, avhistory = 0;

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
            data(personal_data);
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear the input buffer
        }

        // Show the lessons and choose one
        if (menu_choose == 2)
        {
            string choose_lesson = lessons(lessonVector, enter_lesson, math, english, programming, history);

            // Enter grades
            if (choose_lesson != "")
            {
                cout << "You chose " << choose_lesson << "\n";
            }

            cout << "How many grades do you want to enter at " << choose_lesson << " ?\n";
            cin >> num_of_grades;

            // Enter grades for Math
            if (choose_lesson == "Math")
            {
                for (int i = 0; i < num_of_grades; i++)
                {
                    cout << "[" << i + 1 << "] = ";
                    cin >> grade;
                    avmath += grade;
                    math.push_back(grade);
                }
            }

            // Enter grades for English
            if (choose_lesson == "English")
            {
                for (int i = 0; i < num_of_grades; i++)
                {
                    cout << "[" << i + 1 << "] = ";
                    cin >> grade;
                    avenglish += grade;
                    english.push_back(grade);
                }
            }

            // Enter grades for Programming
            if (choose_lesson == "Programming")
            {
                for (int i = 0; i < num_of_grades; i++)
                {
                    cout << "[" << i + 1 << "] = ";
                    cin >> grade;
                    avprogramming += grade;
                    programming.push_back(grade);
                }
            }

            // Enter grades for history
            if (choose_lesson == "History")
            {
                for (int i = 0; i < num_of_grades; i++)
                {
                    cout << "[" << i + 1 << "] = ";
                    cin >> grade;
                    avhistory += grade;
                    history.push_back(grade);
                }
            }
        }

        // Average and data output
        if (menu_choose == 3)
        {
            average(avmath, avenglish, avprogramming, avhistory, math, english, programming, history);
            cout << "Name : " << user.name << " " << user.sname << "\n";
            cout << "About you : " << personal_data << "\n";
            cout << "Math average : " << avmath << "\n";
            cout << "English average : " << avenglish << "\n";
            cout << "Programming average : " << avprogramming << "\n";
            cout << "History average : " << avhistory << "\n";
        }

    } while (menu_choose >= 1 && menu_choose < 4);

    return 0;
}