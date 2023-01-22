#pragma once

#include <string>
#include <vector>

class Category {
public:
  std::string name;
};

class Transaction {
public:
  // Negative for an expense, positive for an income.
  float amount;
  Category category;
};

class Account {
public:
  float Balance() const {
    float balance = 0.0f;

    for (auto t : transactions) {
      balance += t.amount;
    }

    return balance;
  }

  std::vector<Transaction> transactions;
};
