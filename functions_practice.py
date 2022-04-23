from threading import Timer
import socket

name = input("Enter Name ")
last_name = input("Enter Last Name ")


def hello(name):
    print(f"Hello {name}  ")


def pack(first, last, username):
    info = []
    info.extend([first, last, username])
    hello(info[0])
    print(f"Your name is {info[0]} {info[1]} and your social security # is {info[2]}")


pack(name, last_name, "675-32-6593")


def eat_lunch(list):
    for i in range(1):
        print(f"First you will eat {list[0]}")
        print(f"Then you will eat {list[1]}")
        print(f"After you will eat {list[2]}")


eat_lunch(["Silicon", "Copper", "Lithium"])


def last_call():
    print(f"I know you want too.. {name}")


def scary_wait():
    print("Never trust a machine... ")
    Timer(1.5, scary).start()


def scary():
    hiddenIP = socket.gethostbyname(socket.gethostname())
    print(f"This may even be your IP {hiddenIP}")


def decide():
    play = input("Yes or No ")
    cap = play.title()

    if cap == "Yes":
        print(
            f"ballsy, I mean I clearly seem malicious, and actually if I'm not mistaken..."
        )
        Timer(1.3, scary_wait).start()

    else:
        print("Dont be scared.. run me again")
        Timer(0.5, last_call).start()


def whoops():
    print(f"I mean me..")
    Timer(0.7, decide).start()


def playGame():
    print(f"Would you like to play with us?")
    Timer(1.0, whoops).start()


playGame()
