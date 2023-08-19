# For a list of words, print out each word on a separate line,
# but in all uppercase. How can you change a word to uppercase?
# Ask Python for help on what you can do with strings!

words = ["hello", "hey", "goodbye", "yo", "yes"]
for word in words:
    print(word.upper())


# Turn that into a function, print_upper_words.
# Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """Prints out each word on a separate line, but in all uppercase."""
    for word in words:
        print(word.upper())


# Change that function so that it only prints words that
# start with the letter ‘e’ (either upper or lowercase).

def print_upper_words(words):
    """Prints out each word on a separate line, but in all uppercase, if they start with 'e' or 'E'."""
    for word in words:
        if word.upper().startswith("E"):
            print(word.upper())


# Make your function more general: you should be able to pass in a set of
# letters, and it only prints words that start with one of those letters.

def print_upper_words(words, must_start_with):
    """Prints out each word on a separate line, but in all uppercase, if they start with the given letters."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break



