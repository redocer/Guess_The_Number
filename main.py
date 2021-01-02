import random


def func_random_level(level):
    system_number = random.randint(1, level)
    return system_number


if __name__ == '__main__':
    levels = 1
    print("Welcome to the Game of Numbers")
    while levels < 10:
        print("-------Level " + str(levels) + "-------")
        print("Guess the number within range of 1 to " + str(levels+1))
        user_input_number = int(input())
        sys_number = func_random_level(levels+1)
        if user_input_number == sys_number:
            print("Level " + str(levels) + " completed successfully")
        else:
            print("You lost! Please try again.")
            break
        levels = levels + 1
