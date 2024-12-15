import math
from itertools import permutations

# Load the word list - due to licensing reasons I cannot publish the wordlist - this code is defunct and is only used for documentation
def load_words(file_path):
    with open(file_path, "r") as file:
        return {line.strip().upper() for line in file}  # Use a set for O(1) lookups

# Letter scoring system
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 8, 'G': 2, 'H': 8, 'I': 1,
    'J': 16, 'K': 10, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 20, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 8, 'W': 8, 'X': 16, 'Y': 8, 'Z': 20
}

# User input
letters = input("Please enter the letters: ").upper()
teddy = int(input("Is Teddy active? 1 for yes, 0 for no. "))
split_letters = list(letters)

# Load words
words = load_words("WordsList.txt")

# Scoring variables
highscore = 0
best_letters = ""
# Generate permutations
for shuffled_tuple in set(permutations(split_letters)):
    letters_shuffled = list(shuffled_tuple)
    used_words = set()
    score = 0
    tempscore = 0

    # Try all substrings of shuffled letters
    found_word = True
    cascades = 0
    clear_bonus = 0
    words_made_list = []
    word_scores = []
    cleared_list = list(shuffled_tuple)
    while found_word:
        found_word = False
        words_made = 0
        used_letters = set()

        for v in range(len(letters_shuffled) - 2):
            for i in range(len(letters_shuffled)):
                if len(letters_shuffled) - v - 3 >= i:
                    word = "".join(letters_shuffled[i:(len(letters_shuffled) - v)])
                    if (word in words and word not in used_words and 
                        not all(index in used_letters for index in range(i, i + len(word)))):
                        if any(word in x for x in list(used_words)) == False:
                            # Calculate score for the word
                            singlescore = 0
                            found_word = True
                            used_words.add(word)
                            singlescore = sum(letter_scores[letter] for letter in word)
                            if teddy == 1:
                                word_scores.append((singlescore * (2 ** (len(word) - 3))) + 2 * (len(word) - 3))
                            else:
                                word_scores.append(singlescore * (2 ** (len(word) - 3)))
                            #tempscore += (singlescore * (2 ** (len(word) - 3))) + 2 * (len(word) - 3)
                            used_letters.update(range(i, (len(letters_shuffled) - v)))
                            words_made += 1

        if found_word:
            cascades += 1
            if clear_bonus < 1:
                holdlist = [cleared_list[i] for i in used_letters]
                for i, element in enumerate(cleared_list[:]):
                    if i == 0:
                        cleared_list.clear()
                    if i not in used_letters:
                        cleared_list.append(element)
                cleared_list.extend(True for _ in holdlist)
            # Apply bonuses
            if all(element == True for element in cleared_list) or clear_bonus >= 1:
                clear_bonus += 1
            if words_made >= 2:
                words_made_list.append(words_made)
        
        # Remove used letters from letters_shuffled for the next iteration
        hold_letters = [letter for index, letter in enumerate(letters_shuffled) if index in used_letters]
        letters_shuffled = [letter for index, letter in enumerate(letters_shuffled) if index not in used_letters]
        letters_shuffled.extend(hold_letters)

    cascade_score = 10
    multi_word_bonus = 0
    tempscore = 8*teddy
    for h in range(1,cascades-1):
        if (cascades - (cascades - h)) <= 8:
            cascade_score += 10 * (3 ** (cascades - (cascades - h)))
        else:
            cascade_score += (cascades - 8) * (10 * (3 ** 8))
    for wordsMade in words_made_list:
        if teddy == 1:
            multi_word_bonus += (5*(wordsMade-1))+12
        else:
            multi_word_bonus += (5*(wordsMade-1))
    clear_score = 15*len(letters_shuffled)*clear_bonus
    if shuffled_tuple == ('T','U','O','N','E','I'):
        print(cascade_score)
        print(word_scores)
        print(multi_word_bonus)
    tempscore += cascade_score + multi_word_bonus + clear_score + sum(scr for scr in word_scores)
    score += tempscore
    # Update high score if this permutation is better
    if score > highscore:
        print(f"New Best! {''.join(shuffled_tuple)}: {score}")
        highscore = score
        best_letters = ''.join(shuffled_tuple)

# Output results
print("Done")
print(f"Highscore: {highscore}")
print(f"Best Letters: {best_letters}")