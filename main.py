from contextgeneration import load_and_split_doc, generate_context
from init import FILENAME, DELIMITER




if __name__ == "__main__":
    try:
        whole_string, split_strings = load_and_split_doc(FILENAME, DELIMITER)
        # Output the list of split strings
        #for idx, section in enumerate(split_strings):
        #    print(f"Section {idx + 1}:\n{section}\n")
        context = generate_context(whole_string, split_strings)
        newfilename = "contexted_" + FILENAME
        with open(newfilename, 'w') as file:
            for idx, section in enumerate(split_strings):
                file.write(f"+++++ Chunk {idx + 1} of {len(split_strings)} +++++\nOriginal:\n{section}\n\nContext:\n{context[idx]}\n\n")
    except Exception as e:
        print(f"Error: {e}")