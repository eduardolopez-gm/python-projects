import random

words = ["Hello world", "How are you today?", "Greetings from Argentina", "Lorem ipsum"]
word = random.choice(words)
hidden_letters = int(len(word) * 0.6 )
hidden_positions = random.sample(range(len(word)), hidden_letters)

hidden_word = ""
# Convert phrase 
for index, letter in enumerate(word):
    hidden_word += "_" if index in hidden_positions else letter


attempts = 5

while attempts > 0:

    print(f"Guess the phrase: {hidden_word} \n You have {attempts} attempts.")

    text = input("Enter a letter or the final solution: ")

    if len(text) == 1:
        new_hidden_word = ""
        success = False
        for index, letter in enumerate(word):
            if text == letter and hidden_word[index] == "_":
                new_hidden_word += text
                success = True
            else:
                new_hidden_word += hidden_word[index]
        hidden_word = new_hidden_word

        if success:
            if word == hidden_word:
                print(f"Congratulations, you guess the phrase")
                break
            else:
                print("You guess the letter")
        else:
            print("Letter already found or is visible")
            attempts -= 1
    elif len(text) == len(word):
        if text == word:
            print("You guess the phrase. Well done")
            break
        else:
            print("The phrase is not correct")
            attempts -= 1
    else:
        print("Invalid letter")

if attempts == 0:
    print(f"You lose, the hidden phrase is {word}")

#print(word, hidden_letters, hidden_positions, hidden_word)