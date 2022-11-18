import random

try:
    try:
        print("hi")
        print(4664/random.randint(0, 1))
    except NameError as err:
        print(err)
except Exception as err:
    print(err)
else:
    print("code success")
finally:
    print("bye")


def checker(var: str):
    if type(var) == str:
        return var
    raise TypeError(f"Expected value of type 'str', got '{type(var).__name__}' instead")


checker("")

something = [1, 2, 3, 4, 5]
iterator = iter(something)
for elem in iterator:
    print(elem)


def avg(*args):
    return sum(args)/len(args)


print(avg(1, 2, 3))
