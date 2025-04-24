'''
Name: Dylan Phoutthavong
Date: April 21st, 2025
Course: CSCI 3412
Task(s): Q3) (25 points) Develop a "toy" spelling checker application in Python using the bottom-up Levenshtein Edit Distance (LED) algorithm:
'''

import sys
import re
from collections import Counter

# -------------------------------
# Command-line Argument: Number of suggestions
# -------------------------------
TOP_N = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# -------------------------------
# Constants
# -------------------------------
MIN_WORD_LENGTH = 3
MAX_EDIT_DISTANCE = 4

# -------------------------------
# Levenshtein Edit Distance (Bottom-Up)
# -------------------------------
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1] # Substitution
                )
    return dp[m][n]

# -------------------------------
# Build Dictionary (Word → Frequency)
# -------------------------------
def build_dictionary(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
        words = re.findall(r'\b[a-z]+\b', text)
        return Counter(words)

# -------------------------------
# Load Misspelled Words from Text
# -------------------------------
def load_misspelled_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
        words = re.findall(r'\b[a-z]+\b', text)
        return words

# -------------------------------
# Get Spelling Suggestions
# -------------------------------
def get_suggestions(word, dictionary, top_n):
    suggestions = []
    for dict_word in dictionary:
        if abs(len(dict_word) - len(word)) < 4:
            dist = edit_distance(word, dict_word)
            if dist <= MAX_EDIT_DISTANCE and len(dict_word) >= MIN_WORD_LENGTH:
                suggestions.append((dict_word, dist, dictionary[dict_word]))
    suggestions.sort(key=lambda x: (x[1], -x[2]))
    return suggestions[:top_n]

# -------------------------------
# Main Function (writes to file)
# -------------------------------
def main():
    dictionary = build_dictionary("dictionary.txt")
    misspelled_words = load_misspelled_words("misspelled.txt")
    checked = set()

    with open("spell_output.txt", "w") as out:
        out.write(f"Dictionary size: {len(dictionary)}\n")
        out.write("Please enter the file to check for spelling: misspelled.txt\n\n")

        for word in misspelled_words:
            if word in dictionary or word in checked:
                continue
            checked.add(word)
            suggestions = get_suggestions(word, dictionary, TOP_N)
            formatted = ", ".join([f"('{w}', {d}, {f})" for w, d, f in suggestions])
            out.write(f"- Suggestions for '{word}': [{formatted}]\n")

# -------------------------------
# Run the Program
# -------------------------------
if __name__ == "__main__":
    main()