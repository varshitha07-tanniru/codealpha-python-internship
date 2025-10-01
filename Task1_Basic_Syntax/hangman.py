#HANGMAN GAME
import random
oceans = ["indian", "antarctica", "atlantic", "pacific", "arctic"]
print("oceans: ",",".join(oceans))
secret=random.choice(oceans)
result=['-']*len(secret)
guess_letters=set()
ch=6
print("Welcome to Hangman! Guess the ocean name letter by letter.")
print("You have", ch, "chances.")
print("Word to guess:", " ".join(result))
while(ch!=0 and "".join(result)!=secret):
    letter=input("GUESS THE LETTER")
    if letter in guess_letters:
        print("Already guessed! Try a different letter.")
        print()
        continue
    if(letter in secret):
        print("CORRECT GUESS CONTINUE!!")
        print()
        guess_letters.add(letter)
        for i in range(len(secret)):
            if(secret[i]==letter):
                result[i]=letter
        print("Current word:", " ".join(result))
        print()
    else:
        ch-=1
        print("WRONG GUESS!! ONLY ",ch,"chances left")
        print()
if "".join(result) == secret:
    print("HURRAY, YOU WON!!! The word was:", secret)
else:
    print("OOPS, YOU LOST. The word was:", secret)



            
