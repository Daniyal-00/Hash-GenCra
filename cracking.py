# cracking
import csv
from hashing import generate_hash

# cracking hash with Dict
def crack_hash(target_hash, dictionary_file, algorithm):
    try:
        with open(dictionary_file, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                hash_attempt = generate_hash(word, algorithm)
                if hash_attempt == target_hash:
                    return f"Found match: {word}"
        return "No match found."
    except FileNotFoundError:
        return "Dictionary file not found."

# cracking hash from CSV file
def crack_multiple_hashes_from_csv(csv_file, dictionary_file, algorithm):
    results = {}
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row_index, row in enumerate(reader):
                for col_index, target_hash in enumerate(row):
                    # cracking any hash
                    result = crack_hash(target_hash.strip(), dictionary_file, algorithm)
                    results[(row_index + 1, col_index + 1)] = result
        return results
    except FileNotFoundError:
        return "CSV file not found."
