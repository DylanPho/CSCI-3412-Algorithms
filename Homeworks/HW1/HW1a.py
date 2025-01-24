# Name: Dyan Phoutthavong
# Date: Janurary 23rd, 2025
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

def encode_message(message, n):
    encoded = ""
    for char in message:
        if char.isalpha():
            # shift alphabet characters
            base = ord('A') if char.isupper() else ord('a')
            encoded += chr((ord(char) - base + n) % 26 + base)
        elif char.isdigit():
            # shift numeric of characters
            encoded += chr((ord(char) - ord('0') + n) % 10 + ord('0'))
        else:
            # non-alphanumeric characters do not change
            encoded += char
    return encoded

def decode_message(encoded_message, n):
    decoded = ""
    for char in encoded_message:
        if char.isalpha():
            # reverse shift for alphabet characters
            base = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - base - n) % 26 + base)
        elif char.isdigit():
            # reverse shift for numeric characters
            decoded += chr((ord(char) - ord('0') - n) % 10 + ord('0'))
        else:
            # non-alphanumeric characters do not change
            decoded += char
    return decoded

def main():
    # user input
    message = input("Input Message: ")

    # validatge shift value(n)
    while True:
        try:
            n = int(input("Shift(n) 1-25: "))
            if  1 <= n <= 25:
                break
            else:
                print("Error: Shift value must be between 1 and 25.")
        except ValueError:
            print("Error: Shift value must be an interger.")
    
    # encode message
    encoded_message = encode_message(message, n)
    print(f"Encoded Message: {encoded_message}")

    # decode message
    decoded_message = decode_message(encoded_message, n)
    print(f"Decoded Message: {decoded_message}")

# call function 
main()