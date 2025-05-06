'''
Name: Dylan Phoutthavong
Date: May 4th, 2025
Course: CSCI 3412
Task(s): Huffman Coding Function
    Feel free to use any existing Huffman code available on the Internet of your choice.  You may also use the code in the class notes.

    Define a function to generate a Huffman code table.

    1. Prompt the user to enter input text or to specify an input file
    2. Count the frequency of each character in the provided text or file to build a frequency table (Dictionary ADT)
    3. Build a Huffman tree using the frequency table.
    4. Create a Huffman code table based on the Huffman tree.
    5. Then, a dictionary is returned, mapping each character to its Huffman code.  e.g., {('e', 00), ('k', 101), ('s', 1010), ...}
'''

from heapq import heappush, heappop
from collections import defaultdict
from bitarray import bitarray
import math
import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        heappush(heap, HuffmanNode(char, freq))
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush(heap, merged)
    return heap[0]

def build_huffman_code_table(root):
    huffman_code = {}
    def encode(node, code=""):
        if node is None:
            return
        if node.char is not None:
            huffman_code[node.char] = code
        encode(node.left, code + "0")
        encode(node.right, code + "1")
    encode(root)
    return huffman_code

def zip(text, fileName, huffman):
    encoded = ''.join(huffman[char] for char in text)
    bit_stream = bitarray(encoded)
    with open(fileName + ".zip", "wb") as f:
        bit_stream.tofile(f)
    return bit_stream

def unzip(fileName, huffman):
    reverse_huffman = {v: k for k, v in huffman.items()}
    with open(fileName + ".zip", "rb") as f:
        bit_stream = bitarray()
        bit_stream.fromfile(f)
    decoded_text = ""
    current_bits = ""
    for bit in bit_stream.to01():
        current_bits += bit
        if current_bits in reverse_huffman:
            decoded_text += reverse_huffman[current_bits]
            current_bits = ""
    with open(fileName + ".unzipped.txt", "w", encoding="utf-8") as f:
        f.write(decoded_text)
    return decoded_text

def compute_efficiency_stats(text, huffman, encoded_bits):
    ascii_cost = len(text) * 8
    huff_cost = sum(len(huffman[char]) * freq for char, freq in build_frequency_table(text).items())
    fcl_cost = sum(math.ceil(math.log2(len(huffman))) * freq for freq in build_frequency_table(text).values())
    huff_improvement_ascii = round(100 * (1 - huff_cost / ascii_cost))
    huff_improvement_fcl = round(100 * (1 - huff_cost / fcl_cost))
    return {
        "Huffman cost": huff_cost,
        "ASCII cost": ascii_cost,
        "Huffman vs ASCII": f"{huff_improvement_ascii}%",
        "Optimal FCL cost": fcl_cost,
        "Huffman vs FCL": f"{huff_improvement_fcl}%",
        "King.txt size": len(text),
        "King.zip size": len(encoded_bits) // 8,
        "King.unzipped.txt size": len(text)
    }

if __name__ == "__main__":
    file_name = "King.txt"
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()

    freq_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(freq_table)
    huffman_dict = build_huffman_code_table(huffman_tree)

    print(f"{'Character':<10} {'Weight':<10} {'Huffman Code'}")
    print("-" * 40)
    for char, code in sorted(huffman_dict.items(), key=lambda x: freq_table[x[0]], reverse=True):
        display_char = char.replace('\n', '\\n').replace(' ', 'space') if char in ['\n', ' '] else char
        print(f"{display_char!r:<10} {freq_table[char]:<10} {code}")

    bit_stream = zip(text, "King", huffman_dict)
    unzip("King", huffman_dict)

    print("\n--- Compression Stats ---")
    stats = compute_efficiency_stats(text, huffman_dict, bit_stream)
    for k, v in stats.items():
        print(f"{k}: {v}")