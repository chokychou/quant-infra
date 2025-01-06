# gazelle:resolve py src.asset_pb2 :asset_py_proto
load("@protobuf//bazel:py_proto_library.bzl", "py_proto_library")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "asset_proto",
    srcs = ["asset.proto"],
)

py_proto_library(
    name = "asset_py_proto",
    deps = [":asset_proto"],
)

py_binary(
    name = "service",
    srcs = ["service.py"],
    visibility = ["//:__subpackages__"],
    deps = ["@pip//schwabdev"],
)

py_library(
    name = "src",
    srcs = [
        "market.py",
        "service.py",
        "strategy.py",
    ],
    visibility = ["//:__subpackages__"],
    deps = [
        ":asset_py_proto",
        "@pip//schwabdev",
    ],
)

py_test(
    name = "market_test",
    srcs = ["market_test.py"],
)

py_test(
    name = "strategy_test",
    srcs = ["strategy_test.py"],
    deps = [
        ":asset_py_proto",
        ":src",
    ],
)
