import random
print('What is your name?')
name = input()
secretnumber = random.randint(1,20)
print('Well,'  + name + ' Guess a number between 1 and 20')
rightguess = False
try:
    for guesstaken in range (1,7):
        print('Take a guess')
        guess=input()
        if int(guess) == secretnumber:
            print('Great! you guessed it correctly')
            rightguess = True
            break
        elif int(guess) < secretnumber:
            print('Your guess is too low. guess number ' + str(guesstaken))
        elif int(guess) > secretnumber:
            print('Your guess is too high. guess number ' + str(guesstaken))
    if not rightguess:            
        print('You have lost all option. I was thinkging of ' + str(secretnumber) )
except ValueError:
    print('Wrong input')
except TypeError:
    print('Enter Int input')
        
