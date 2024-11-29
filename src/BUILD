load("@rules_python//python:defs.bzl", "py_binary")

py_library(
    name = "account",
    srcs = ["account.py"],
)

py_library(
    name = "market",
    srcs = ["market.py"],
)

py_binary(
    name = "service_binary",
    srcs = ["service.py"],
    main = "service.py",
    visibility = ["//mpm:__subpackages__"],
    deps = [
        ":account",
        ":market",
    ],
)
