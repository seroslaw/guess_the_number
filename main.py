from random import randint

def numbers_validation(*numb):
    #print(type(numb[0]))
    #print(type(numb[1]))
    if numb[0] > 0 and numb[0] < 4 and numb[1] > 0 and numb[1] < 11:
        return True
    else:
        return False

if __name__ == '__main__':

    position = 'start'
    while position:

        # How many times the user will play
        tries_number_input = input("How many tries do you want to have? Only 1-3 tries are allowed: ")
        tries_number = int(tries_number_input)

        # User tell us the range of numbers
        range_input = input("Tell the range between 1-10: ")
        range = int(range_input)

        print(numbers_validation(tries_number, range))          #dla przeczytania wartości

        if numbers_validation(tries_number, range) != True:
            accept = input("Your tries number or range number is incorrect. Do you want try again? Type: Yes or No.")
            if accept == "yes" or accept == "Yes":
                print("You decided to try one more time ! great :)")
                continue
            elif accept == "no" or accept == "No":
                print("Thank you and see you later! :)")
                exit()
            else:
                print("Program ends because you type bad value! Try run it again.")
        else:
            break

    rand_number = randint(1, range)
    print(f"Random number is: {rand_number}")

    i = 1
    while i <= tries_number:
        #print(i)
        users_numb = input(f"Attempt: {i} - type your number: ")
        users_numb_int = int(users_numb)

        if users_numb_int > range or users_numb_int < 1:
            if i < tries_number:
                print("Your typed number is incorrect - it's out of range. Attempt failed.")
                i += 1
                continue
            else:
                print("Your number is incorrect. It was your last change! You have lost!")
                break
        elif users_numb_int != rand_number:
            if i < tries_number:
                print("Your number is incorrect. Try again.")
                i += 1
                continue
            elif i == tries_number:
                print("Your number is incorrect. It was your last chance! You have lost!")
                break
        else:
            print("Your number is correct! You won - GoOoD JoOoB!")
            break

print("Game ended.")









