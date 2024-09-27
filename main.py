import os
import ollama


def load_and_split_doc(file_path, delimiter):
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

    return file_content, stripped_content

def generate_context(document, chunklist):
    context_responses = []
    try:
        for idx, section in enumerate(chunklist):
            contextprompt = f"""\
<document>
{document}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{section}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else."""
            result = ollama.generate(model="llama3.1:8b-instruct-q8_0", prompt=contextprompt, options={"num_ctx":131072})
            context_responses.append(result.get('response'))
    except Exception as e:
        print(f"Error: {e}")
    return context_responses

if __name__ == "__main__":
    # Replace with your file path and delimiter
    file_path = "test.txt"
    delimiter = "-+-+-+-"

    try:
        whole_string, split_strings = load_and_split_doc(file_path, delimiter)
        # Output the list of split strings
        for idx, section in enumerate(split_strings):
            print(f"Section {idx + 1}:\n{section}\n")
        context = generate_context(whole_string, split_strings)
        for idx, section in enumerate(split_strings):
            print(f"+++++ Chunk {idx + 1} of {len(split_strings)} +++++\nOriginal:\n{section}\n\nContext:\n{context[idx]}\n\n")
    except Exception as e:
        print(f"Error: {e}")