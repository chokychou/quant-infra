load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "auth",
    srcs = ["auth.py"],
    deps = [
        requirement("schwabdev"),
    ],
)

py_library(
    name = "market",
    srcs = ["market.py"],
)

py_library(
    name = "strategy",
    srcs = ["strategy.py"],
    deps = [":market"],
)

py_test(
    name = "market_test",
    srcs = ["market_test.py"],
    deps = [
        ":market",
    ],
)

py_test(
    name = "strategy_test",
    srcs = ["strategy_test.py"],
    deps = [
        ":strategy",
        ":market",
    ],
)

# TODO: Implement service_binary
py_binary(
    name = "service_binary",
    srcs = ["service.py"],
    main = "service.py",
    visibility = ["//mpm:__subpackages__"],
    deps = [
        ":strategy",
        ":market",
    ],
)
