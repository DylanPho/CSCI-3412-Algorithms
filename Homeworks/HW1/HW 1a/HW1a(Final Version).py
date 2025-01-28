# Name: Dyan Phoutthavong
# Date: Janurary 24th, 2025
# Course: 3412 - Algorithms
# Task: 
    # User Input: 
        # Accept an integer n (1-25) and an input string message from the user.

    # Substitution Cipher:
        # Encode the message using a simple substitution cipher where each letter is replaced by the letter that comes n positions later in the alphabet.
            # Example: If n = 3, 'a' becomes 'd', 'b' becomes 'e', and so on. Letters wrap around ('x' becomes 'a').
        # Handle uppercase, lowercase, and numeric characters. Non-alphanumeric characters (e.g., punctuation, spaces) should remain unchanged.

    # Decoding Function:
        #Implement a decoding function that reverses the encoding process to return the original message.

    # Driver Code:
        # Write a main() function to demonstrate your program's correctness by:
            # Accepting input.
            # Encoding the message.
            # Decoding the encoded message.
            # Printing the original, encoded, and decoded messages.
    
    # Hints: 
    # You can use the ord() function to get the Unicode code point of a character and the chr() function to convert a code point back to a character.

# revised code

def shift_character(char, n, direction=1):
    """Shift a single character (alphabet or digit) based on the direction."""
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + direction * n) % 26 + base)
    elif char.isdigit():
        return chr((ord(char) - ord('0') + direction * n) % 10 + ord('0'))
    else:
        return char
    
def transform_message(message, n, direction=1):
    """Transform message by shifting its characters."""
    return ''.join(shift_character(char, n, direction) for char in message)

def main():
    # user input
    message = input("Input Message: ")

    # validate if shift value is in range
    while True:
        try:
            n = int(input("Shift (n) 1-25: "))
            if 1 <= n <= 25:
                break
            else:
                print("Error: Shift value must be between 1 and 25.")
        except ValueError:
            print("Error: Shift value must be an integer.")
    
    # encode and decode message
    encoded_message =  transform_message(message, n, direction=1)
    print(f"Encoded Message: {encoded_message}")

    decoded_message = transform_message(encoded_message, n, direction=1)
    print(f"Decoded Message: {decoded_message}")

main()