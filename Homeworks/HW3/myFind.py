#!/usr/bin/python3
import os
import stat
import sys

def process_file(filepath, file_stat, search_term, results):
    """ Callback function to process found files """
    if search_term in os.path.basename(filepath):  # Match search term in filename
        file_size = file_stat.st_size
        results.append((filepath, file_size))
        return file_size
    return 0

def myFind(directory, search_term, callback, results):
    total_size = 0  # Store total size of matched files

    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            try:
                file_stat = os.stat(full_path)

                if stat.S_ISREG(file_stat.st_mode):  # Regular files only
                    total_size += callback(full_path, file_stat, search_term, results)
                
                elif stat.S_ISDIR(file_stat.st_mode):  # Recursively search directories
                    total_size += myFind(full_path, search_term, callback, results)

            except PermissionError:
                print(f"Permission denied: {full_path}")
                continue

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing {directory}: {e}")
        return 0

    return total_size

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: myFind.py <directory> <search_term>")
        sys.exit(1)

    directory = sys.argv[1]
    search_term = sys.argv[2]
    results = []

    total_size = myFind(directory, search_term, process_file, results)

    for file_path, size in results:
        print(f"{file_path} {size} bytes")

    print(f"Total file size: {total_size} bytes")
