def greet(name):
    return f"Hello, {name}"
if __name__ == "__main__":
    user_name = input("Enter a name: ")
    print(greet(user_name))