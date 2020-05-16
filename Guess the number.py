import random

random_number = random.randint(1, 100)


def guess_the_number():
    for i in range(1, 100):
        while True:
            try:
                your_number = int(input("Please input your number: "))
                break
            except ValueError:
                print("It\'s not a number!")
        if your_number > random_number:
            print("To big")
        elif your_number < random_number:
            print("To small")
        elif your_number == random_number:
            return f"You win your number = {your_number}, random number = {random_number}"


if __name__ == '__main__':
    print(guess_the_number())
