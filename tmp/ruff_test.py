import os

x = 1
y = 2
z = x + y


def greet(name: str) -> str:
    return "hello " + name


greet("123")

x: str = "not an int"


def foo(a, b):
    return a + b


foo(1, 2)
