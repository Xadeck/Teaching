cc_library(
    name = "money",
    srcs = ["money.cc"],
    hdrs = ["money.h"],
)

cc_test(
    name = "money_test",
    srcs = ["money_test.cc"],
    deps = [
        ":money",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_binary(
    name = "main",
    srcs = ["main.cc"],
)
