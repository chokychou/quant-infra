load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_binary(
    name = "service",
    srcs = ["service.py"],
    visibility = ["//:__subpackages__"],
)

py_library(
    name = "src",
    srcs = [
        "auth.py",
        "market.py",
        "service.py",
        "strategy.py",
    ],
    visibility = ["//:__subpackages__"],
    deps = ["@pip//schwabdev"],
)

py_test(
    name = "market_test",
    srcs = ["market_test.py"],
    deps = [":src"],
)

py_test(
    name = "strategy_test",
    srcs = ["strategy_test.py"],
    deps = [":src"],
)
