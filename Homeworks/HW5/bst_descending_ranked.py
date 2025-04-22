from BinarySearchTree import Tree

def load_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            for part in line.strip().split():
                if part.isdigit():
                    numbers.append(int(part))
    return numbers

def main():
    filename = "rand1000.txt"
    numbers = load_numbers(filename)

    tree = Tree()
    for num in numbers:
        tree.insert(num)

    print(f"\nDescending order traversal of {len(numbers)} values with ranking:\n")

    for rank, value in enumerate(tree.descending_generator(), start=1):
        print(f"[{rank}] {value}")

if __name__ == "__main__":
    main()