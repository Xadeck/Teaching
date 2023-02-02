#include "money.h"
#include "gtest/gtest.h"

TEST(MoneyTest, Works) {
  Account account;

  account.transactions.push_back({
      .amount = 217,
      .category = {.name = "Salary"},
  });

  account.transactions.push_back({
      .amount = -100,
      .category = {.name = "Food"},
  });
  EXPECT_EQ(account.Balance(), 117);

  account.transactions.push_back({
      .amount = -50,
      .category = {.name = "Food"},
  });
  EXPECT_EQ(account.Balance(), 67);
}
