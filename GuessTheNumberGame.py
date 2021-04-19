from random import randint
def guess_the_number():
    """Game which asks user about a number. While guessed game is won.
    Otherwise gives user one of two tips : "too small" or "too big".
    Prints an error message while not integer is given. Limitless attempts.
     """
    guessed = False
    machine_rnd = randint(1, 101)
    #print(machine_rnd)
    while not guessed:
        user_attempt = input("Guess the Number: ")
        try:
            num = int(user_attempt)
            if num == machine_rnd:
                print("You win!")
                guessed = True
            elif num < machine_rnd:
                print("Too small!")
            else:
                print("Too big!")
        except ValueError:
            print("It's not a number :)")
            continue
if __name__ == '__main__':
    guess_the_number()