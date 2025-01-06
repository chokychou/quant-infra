load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "asset_parsers",
    srcs = ["backtest_to_asset_parser.py"],
    visibility = ["//:__subpackages__"],
)

py_test(
    name = "asset_parsers_test",
    srcs = ["asset_parsers_test.py"],
    deps = [
        ":asset_parsers",
        "//test/data:data_import_test",
    ],
)
