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
