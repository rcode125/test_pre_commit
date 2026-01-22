def foo(x: int, y: int) -> int:
    if x > 10:
        print("Value is greater than 10")
        return x + y
    else:
        print("small")
        return x - y
