# Import required libraries
import hashlib
import sys, os
import pyperclip
import time

# ASCII Banner
banner = r"""
 _____ _ _        _   _           _        ____ _               _             
|  ___(_) | ___  | | | | __ _ ___| |__    / ___| |__   ___  ___| | _____ _ __ 
| |_  | | |/ _ \ | |_| |/ _` / __| '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
|  _| | | |  __/ |  _  | (_| \__ \ | | | | |___| | | |  __/ (__|   <  __/ |   
|_|   |_|_|\___| |_| |_|\__,_|___/_| |_|  \____|_| |_|\___|\___|_|\_\___|_|   
"""

# Function to select file to check and algorithm
def select():
    # ASCII Art
    print(banner)

    # Greet user
    print("Welcome to File Hash Checker!")
    print("View this tools' source code here: https://github.com/ollieistic/cybertools")

    # Ask for file path
    print("\nInput the path to the file you want to check:")
    file_path = input("> ").strip()

    # Available hash algorithms
    options = {
        'md5', 
        'sha1', 
        'sha224', 
        'sha256', 
        'sha384', 
        'sha512', 
        'sha3_256',
        'blake2b', 
        'blake2s'
    }

    print("\n-------------------------------------------")
    print("Which hash algorithm(s) do you want to use?")
    print("You can use multiple algorithms, separated by commas. Example: md5,sha256")
    print("\nAlgorithms:", ", ".join(sorted(options)))


    choice = input("> ").lower().replace(' ', '')
    selected = set(choice.split(','))

    # Validate selection
    valid = selected.intersection(options)
    if not valid:
        print("\nNo valid algorithm(s) was selected. Default to 'all'.")
        valid = options
    
    print("\nChecking for hashes...")
    time.sleep(1.5)
    return file_path, valid

# Function to calculate hashes
def calculate(file_path, algorithms):
    hashes = {}

    hash_options = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
        'sha3_256': hashlib.sha3_256,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s,
    }

    try:
        with open(file_path, "rb") as f:
            file_data = f.read()

            for algorithm in algorithms:
                if algorithm in hash_options:
                    hash_obj = hash_options[algorithm](file_data)
                    hashes[algorithm] = hash_obj.hexdigest()

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return hashes


# Function to compare found hashes with another
def compare(hashes):
    if not hashes:
        print("\nNo hashes available to compare.")
        return

    print("\nDo you want to compare one of the calculated hashes with a hash you provide? (y/n)")
    choice = input("> ").strip().lower()

    if choice != 'y':
        return

    if len(hashes) == 1:
        algo = next(iter(hashes))
    else:
        print("\nWhich hash algorithm do you want to compare?")
        for algo in hashes:
            print(f"- {algo}")
        algo = input("> ").strip().lower()
        if algo not in hashes:
            print("\nInvalid algorithm selected. Comparison cancelled.")
            return

    print("-------------------------------------------")
    print(f"\nEnter the hash to compare with the calculated {algo.upper()} hash:")
    user_hash = input("> ").strip().lower()

    calculated_hash = hashes[algo].lower()

    time.sleep(1)
    
    if user_hash == calculated_hash:
        print("\n✅ Hashes match!")
    else:
        print("\n❌ Hashes do NOT match.")

    time.sleep(1.5)


# Function to copy results to clipboard
def copy_hashes(hashes):
    if not hashes:
        print("\nNo hashes to copy.")
        return

    print("\nDo you want to copy one of the hashes to your clipboard? (y/n)")
    choice = input("> ").strip().lower()

    if choice != 'y':
        return

    # Copy if there's only one choice
    if len(hashes) == 1:
        algo, value = next(iter(hashes.items()))
        pyperclip.copy(value)
        print(f"\n{algo.upper()} hash copied to clipboard.")
        return

    # Ask which hash to copy when there are mutliple
    print("\nWhich hash do you want to copy?")
    for algo in hashes:
        print(f"- {algo}")

    algo_choice = input("> ").strip().lower()

    if algo_choice in hashes:
        pyperclip.copy(hashes[algo_choice])
        print(f"\n{algo_choice.upper()} hash copied to clipboard.")
    else:
        print("\nInvalid selection.")


# Main function
def main():
    file_path, selected_algorithms = select()

    results = calculate(file_path, selected_algorithms)

    print("\nCalculated Hashes:")
    print("-------------------------------------------")
    for algo, hash_value in results.items():
        print(f"{algo.upper()}: {hash_value}")
    
    compare(results)
    copy_hashes(results)
    

# Call main function
if __name__ == "__main__":
    main()
    print("\nThank you for using File Hash Checker!")