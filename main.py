def greet(name):
    return f"Hello, {name}"


def farewell(name):
    return f"Goodbye, {name}"
if __name__ == "__main__":
    user_name = input("Enter a name: ")
    print(greet(user_name))
    print(farewell(user_name))
    print("text2")
    print("Final")