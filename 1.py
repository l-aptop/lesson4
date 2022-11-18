result = []


def divider(a: int | float, b: int | float):
    try:
        a = float(a)
        b = float(b)
    except TypeError:
        pass
    if type(a) is not float:
        raise TypeError(f"Expected type 'float', got '{type(a).__name__}' instead")
    if type(b) is not float:
        raise TypeError(f"Expected type 'float', got '{type(b).__name__}' instead")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a/b


data = {10.0: 2, 2: 5, "123": 4, 18: 0, 0: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

print(result)
