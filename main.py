import os
from contextgeneration import load_and_split_doc, generate_context
from init import DELIMITER, DOCFOLDER

def get_docs_list(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def process_document(filename, folder_path):
    file_path = os.path.join(folder_path, filename)
    whole_string, split_strings = load_and_split_doc(file_path, DELIMITER)
    context = generate_context(whole_string, split_strings)
    
    newfilename = os.path.join(DOCFOLDER, f"contexted_{filename}")
    with open(newfilename, 'w') as file:
        for idx, section in enumerate(split_strings):
            file.write(f"+++++ Chunk {idx + 1} of {len(split_strings)} +++++\nOriginal:\n{section}\n\nContext:\n{context[idx]}\n\n")
    
    print(f"Processed {filename}. Output saved to {newfilename}")

if __name__ == "__main__":
    try:
        print("Welcome to the proof of concept context generator for RAG.")
        print(f"Searching for files in {DOCFOLDER}...")
        
        docs_list = get_docs_list(DOCFOLDER)
        
        if not docs_list:
            print("No documents found in the specified folder.")
            exit()
        
        print("Found the following documents:")
        for idx, doc in enumerate(docs_list, 1):
            print(f"{idx}. {doc}")
        
        user_input = input("Do you want to continue processing these documents? (Y/N): ").strip().lower()
        
        if user_input != 'y':
            print("Operation cancelled.")
            exit()
        
        for filename in docs_list:
            print(f"\nProcessing {filename}...")
            process_document(filename, DOCFOLDER)
        
        print("\nAll documents have been processed.")
    
    except Exception as e:
        print(f"Error: {e}")