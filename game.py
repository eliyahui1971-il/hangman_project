import random

# Hangman 7 stages
hangman_7_stages = {
    1: """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    2: """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    3: """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    4: """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    5: """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    6: """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    7: """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
}

# Word list
list_of_words = ["Israel","Lebanon","Saudi-Arabia","Jordan","Iran","iraq","USA"]



# Choose random word & clear non CHR
def choose_random_word():
    word_to_process=random.choice(list_of_words).lower()
    clear_word =""
    not_required=""
    for char in word_to_process:
        if char.isalpha():
            clear_word+=char
        else:
            not_required+=char
    return clear_word


# Display current word state
def display_word_state(word, guessed_letters):
    word_staus=" ".join([letter if letter in guessed_letters else "_" for letter in word])
    return word_staus

# Display hangman stage
def display_hangman_stage(wrong_guesses):
    print(hangman_7_stages[wrong_guesses])

# Initialize alphabet pool manually
def initialize_alphabet_pool():
    return list("abcdefghijklmnopqrstuvwxyz")

# Get guess from user
def get_guess(available_letters):
    print("Available letters:", " ".join(available_letters))
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return None
    if guess not in available_letters:
        print("Letter already chosen or not available.")
        return None
    return guess

# Main game function
def play_hangman():
    word = choose_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(hangman_7_stages)

    available_letters = initialize_alphabet_pool()
    correct_letters = []
    incorrect_letters = []

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")
    print(display_word_state(word, guessed_letters))

    while wrong_guesses < max_wrong and "_" in display_word_state(word, guessed_letters):
        guess = get_guess(available_letters)
        if not guess:
            continue

        available_letters.remove(guess)

        if guess in word:
            guessed_letters.add(guess)
            correct_letters.append(guess)
            print("Correct! Current word:", display_word_state(word, guessed_letters))
            print("Correct letters so far:", " ".join(correct_letters))
        else:
            wrong_guesses += 1
            incorrect_letters.append(guess)
            print("Wrong! You have", max_wrong - wrong_guesses, "lives left.")
            display_hangman_stage(wrong_guesses)
            print("Incorrect letters so far:", " ".join(incorrect_letters))

    if "_" not in display_word_state(word, guessed_letters):
        print("You win! The word was:", word)
    else:
        print("You lose! The word was:", word)

# Entry point
if __name__ == "__main__":
    play_hangman()