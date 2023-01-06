#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

// 2. I need to create the ability to choose to put income or expenses - ✓
// 4. I need to let the user to choose the category - ✓
// 5. I need to let the user to put the amount - ✓
// 6. I need to let the user to see the balance - ✓
// 7. I need to let the user to see the statistics - ✓
// 8. I need to fix bugs :) -

/*
THE LIST OF SOLVED BUGS :
 - If the user enters a value that is not between 1 and 3 (for income) or 1 and 5 (for expense),
the program will still execute the corresponding menu option. - ✓

 - When I check one time the Statistics , and after I put some income or expense for example ,
  when I check statistics second time it shows me all the data that was there until I checked the statistics,
   but it doesn't show me the data that I entered after I checked the statistics for the first time -
*/

void income_expense() // Menu
{
    cout << "**********************************************************************************" << endl;
    cout << "Choose |1|Income |2|Expense |3|Balance |4|Stastistics  (press other key for Exit)" << endl;
    cout << "**********************************************************************************" << endl;
}

void category_income() // Income categories
{
    int user_category_inc;
    cout << "Choose the category of income : " << endl;
    cout << "|1|Salary |2|Bonus |3|Other" << endl;
    cout << "Choose (1 to 3) : ";
}

void category_expense() // Expense categories
{
    int user_category_exp;
    cout << "\nChoose the category of expense : ";
    cout << "\n|1|Food |2|Social Life |3|Self Development |4|Transportation |5|Other" << endl;
    cout << "Choose (1 to 5) : ";
}

int main()
{
    fstream File;
    File.open("statistic.txt", ios::out);

    // Variables that I will need in program
    double balance = 0;
    double income = 0;
    double expense = 0;
    int income_expense_choose = 0;
    string stastistic_income;
    string stastistic_expense;

    string income_array[3] = {"Salary", "Bonus", "Other"};
    string expense_array[5] = {"Food", "Social Life", "Self Development", "Transportation", "Other"};

    do // The steps
    {
        income_expense();
        cout << "Enter your choice (1 to 4) : ";
        cin >> income_expense_choose;

        system("cls");

        // The steps for income


        if (income_expense_choose == 1)
        {
            category_income();
            int category_income_choose;
            cin >> category_income_choose;

            if (category_income_choose < 1 || category_income_choose > 3)
            {
                cout << "Invalid category choice. Please try again." << endl;
                continue;
            }

            stastistic_income = income_array[category_income_choose - 1];
            File << "INCOME : " << stastistic_income << " - ";

            cout << "Enter the Income : ";
            cin >> income;
            File << income << " $" << endl;
            balance += income;
        }
        //_____________________________________________________________________________________________________________________________________________
        // The steps for expense
        if (income_expense_choose == 2)
        {
            category_expense();
            int category_expense_choose;
            cin >> category_expense_choose;

            if (category_expense_choose < 1 || category_expense_choose > 5)
            {
                cout << "Invalid category choice. Please try again." << endl;
                continue;
            }
            else

                stastistic_expense = expense_array[category_expense_choose - 1];
            File << "EXPENSE : " << stastistic_expense << " - ";

            cout << "Enter the Expense : ";
            cin >> expense;
            File << expense << " $" << endl;
            balance -= expense;
        }
        //_____________________________________________________________________________________________________________________________________________
        // The steps for Balance
        if (income_expense_choose == 3)
        {
            cout << "\nYour balance : " << balance << " $" << endl;
        }
        //_____________________________________________________________________________________________________________________________________________
        // The steps for statistics
        if (income_expense_choose == 4)
        {
            File.open("statistic.txt", ios::in);
            if (File.is_open())
            {
                string line;
                while (getline(File, line))
                {
                    cout << line << endl;
                }
            }
            File.close();
        }

    } while (income_expense_choose < 5 && income_expense_choose > 0);

    return 0;
}