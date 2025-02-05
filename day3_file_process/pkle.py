import pickle

# d = [10, 20, 30, 40, 50]
# file = open("day3\\test.txt", "wb")
# pickle.dump(d, file)
# file.close()
# l = pickle.load(open("day3\\test.txt", "rb"))
# print(l)
import re
import pickle

# Function to extract and dump dictionaries from a text file


def extract_and_dump_dicts(file_path, output_path):
    with open("day3\\pkle.txt", 'r') as file:
        content = file.read()

    # Regex pattern to identify dictionary-like structures
    dict_pattern = re.compile(r'\{[^{}]*\}')

    # Find all matches
    dicts = dict_pattern.findall(content)

    # Convert and dump dictionaries
    extracted_dicts = []
    for d in dicts:
        try:
            # Safely evaluate the dictionary string
            extracted_dicts.append(eval(d))
        except (SyntaxError, NameError):
            continue  # Skip invalid dictionary-like patterns

    # Dump to a text file using pickle
    with open(output_path, 'wb') as output_file:
        pickle.dump(extracted_dicts, output_file)

# Function to load and verify the dumped dictionaries


def load_and_verify_dicts(output_path):
    with open(output_path, 'rb') as input_file:
        loaded_dicts = pickle.load(input_file)
        return loaded_dicts


# Example usage
input_file = 'pkle.txt'   # Replace with your actual file name
output_file = 'output.txt'

extract_and_dump_dicts(input_file, output_file)

# Verifying the data
verified_dicts = load_and_verify_dicts(output_file)
print(verified_dicts)
