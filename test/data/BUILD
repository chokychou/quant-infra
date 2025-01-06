load("@rules_python//python:defs.bzl", "py_test")

package(default_visibility = ["//visibility:public"])

filegroup(
    name = "test_data",
    srcs = glob(["**/*.feather"]),
    visibility = ["//:__subpackages__"],
)

py_test(
    name = "data_import_test",
    srcs = ["data_import_test.py"],
    data = [":test_data"],
    deps = [
        "@pip//numpy",
        "@pip//pandas",
        "@pip//pyarrow",
    ],
)
