import random
words = ["python","computer","prongram","keyboard","hangman","coding"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("==== HANGMAN GAME ====")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_"
    print("\nWord:", display)

    if "_" not in display:
        print("Congratulation you guessed word:", word)
        break
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    if guess not in word:
        attempts -= 1
        print("X wrong guess!")
        print("Attempts left:", attempts)
    if attempts == 0:
        print("\n Game over")
        print("The correct word was:", word)
