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

// Lessons function
string lessons(vector<string> lessonVector)
{
}

int main()
{

    Student user;

    // Enter the name
    cout << "Enter your first name : ";
    cin >> user.name;
    cout << "Enter your second name : ";
    cin >> user.sname;

    // Show the lessons and choose one
    vector<string> lessonVector = {"Math", "English", "Programming", "History"};
    cout << "Your lessons are : ";
    for (int i = 0; i < lessonVector.size(); i++)
    {

        cout << i + 1 << "." << lessonVector[i] << " | ";
    }

    int enter_lesson = 0;
    cout << "Choose your lesson : ";
    cin >> enter_lesson;
    string choose_lesson = lessonVector[enter_lesson - 1];
    cout << "Your lesson is : " << choose_lesson;
}