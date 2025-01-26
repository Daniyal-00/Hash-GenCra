# main
from hashing import generate_hash, generate_hash_from_csv
from cracking import crack_hash, crack_multiple_hashes_from_csv

def save_to_file(results, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in results:
                file.write(line + "\n")
        print(f"Results have been saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

def user_input():
    algorithm = input("Enter the hashing algorithm (e.g., sha256, md5, sha1): ").strip().lower()
    
    action = input("Would you like to (1) Generate hash or (2) Crack hash? Enter 1 or 2: ").strip()

    if action == '1':
        choice = input("Would you like to (1) Hash a text or (2) Hash from CSV? Enter 1 or 2: ").strip()
        if choice == '1':
            text = input("Enter the text to hash: ").strip()
            hash_result = generate_hash(text, algorithm)
            print(f"Generated Hash: {hash_result}")
            # save result's
            save_option = input("Do you want to save the hash to a file? (yes/no): ").strip().lower()
            if save_option == 'yes':
                filename = input("Enter the file name to save the result (e.g., result.txt): ").strip()
                save_to_file([hash_result], filename)
        elif choice == '2':
            csv_file = input("Enter the CSV file path to hash: ").strip()
            hash_results = generate_hash_from_csv(csv_file, algorithm)
            print(f"Generated Hashes: {hash_results}")
            # save result's
            save_option = input("Do you want to save the hashes to a file? (yes/no): ").strip().lower()
            if save_option == 'yes':
                filename = input("Enter the file name to save the result (e.g., result.txt): ").strip()
                save_to_file(hash_results, filename)
        else:
            print("Invalid choice.")
    elif action == '2':
        choice = input("Would you like to (1) Crack Simple Hash or (2) Crack from CSV file? Enter 1 or 2: ").strip()
        if choice == '1':
            target_hash = input("Enter the hash to crack: ").strip()
            dictionary_file = input("Enter the dictionary file path: ").strip()
            result = crack_hash(target_hash, dictionary_file, algorithm)
            print(result)
            # save result's
            save_option = input("Do you want to save the result to a file? (yes/no): ").strip().lower()
            if save_option == 'yes':
                filename = input("Enter the file name to save the result (e.g., result.txt): ").strip()
                save_to_file([result], filename)
        elif choice == '2':
            csv_file = input("Enter the CSV file path containing hashes: ").strip()
            dictionary_file = input("Enter the dictionary file path: ").strip()
            results = crack_multiple_hashes_from_csv(csv_file, dictionary_file, algorithm)
            if isinstance(results, dict):
                result_lines = [f"Row {position[0]}, Column {position[1]}: {result}" for position, result in results.items()]
                for line in result_lines:
                    print(line)
                # save result's
                save_option = input("Do you want to save the results to a file? (yes/no): ").strip().lower()
                if save_option == 'yes':
                    filename = input("Enter the file name to save the result (e.g., result.txt): ").strip()
                    save_to_file(result_lines, filename)
            else:
                print(results)
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    user_input()
