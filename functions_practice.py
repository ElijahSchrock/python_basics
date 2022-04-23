name = input("Enter Name ")
last_name = input("Enter Last Name ")


def hello(name):
    print(f"Hello {name}")


def pack(first, last, username):
    info = []
    info.extend([first, last, username])
    hello(info[0])
    print(f"Your name is {info[0]} {info[1]} and your social is {info[2]}")


pack(name, last_name, "675-32-6593")


def eat_lunch(list):
    for i in range(1):
        print(f"First you will eat {list[0]}")
        print(f"Then you will eat {list[1]}")
        print(f"After you will eat {list[2]}")


eat_lunch(["Apples", "Oranges", "Pizza"])
