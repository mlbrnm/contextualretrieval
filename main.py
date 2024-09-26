import os

def load_and_split_file(file_path, delimiter):
    """
    Loads a file from the specified path and splits its content 
    by the given delimiter, returning the split parts as a list of strings.

    Args:
        file_path (str): The full path to the file to be loaded.
        delimiter (str): The string that will be used to split the file.

    Returns:
        list: A list of strings, each representing a split section of the file.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at path {file_path} does not exist.")
    
    # Read the entire content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Split the file content using the specified delimiter
    split_content = file_content.split(delimiter)
    
    # Apply .strip() to remove leading/trailing whitespace from each section
    stripped_content = [section.strip() for section in split_content]

    return stripped_content


if __name__ == "__main__":
    # Replace with your file path and delimiter
    file_path = "test.txt"
    delimiter = "-----------------"

    try:
        split_strings = load_and_split_file(file_path, delimiter)
        # Output the list of split strings
        for idx, section in enumerate(split_strings):
            print(f"Section {idx + 1}:\n{section}\n")
    except Exception as e:
        print(f"Error: {e}")
