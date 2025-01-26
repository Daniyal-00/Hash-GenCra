# hashing
import hashlib
import csv

# Simple
def generate_hash(text, algorithm):
    try:
        hash_object = hashlib.new(algorithm)
        hash_object.update(text.encode('utf-8'))
        return hash_object.hexdigest()
    except ValueError:
        return "Invalid algorithm selected."
    

# from CSV file
def generate_hash_from_csv(csv_file, algorithm):
    hashes = []
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for text in row:
                    hashes.append(generate_hash(text, algorithm))
        return hashes
    except FileNotFoundError:
        return "CSV file not found."
