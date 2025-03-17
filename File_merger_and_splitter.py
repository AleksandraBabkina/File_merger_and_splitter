import os

# Function to create a directory if it doesn't exist
def create_dir(directory):
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

# Function to merge multiple files into one
def several_to_one(new_file_name, path_to_new_file='/path/to/save/', path_to_folder='/path/to/files/', delim='\n'):
    # Ensure the paths end with a slash
    path_to_new_file = os.path.join(path_to_new_file, '')
    path_to_folder = os.path.join(path_to_folder, '')
    
    # Create the directory to save the new file
    create_dir(path_to_new_file)

    # Get the list of files in the source folder
    files = os.listdir(path_to_folder)
    print(f"Found files: {files}")

    # Open the new file in write mode
    with open(os.path.join(path_to_new_file, new_file_name), 'w', encoding='utf-8-sig') as f_new:
        # Loop through all files in the folder
        for file in files:
            # Skip hidden files or unwanted files
            if file.startswith('.') or file == 'new_dir':
                continue
            # Read the content of each file
            with open(os.path.join(path_to_folder, file), 'r', encoding='utf-8-sig') as f:
                text = f.read()
                # Remove newline and carriage return characters and empty lines
                text = text.replace('\n', ' ').replace('\r', '').strip()
                if text:  # Check if text is not empty
                    f_new.write(text + delim)

# Function to split a single file into several parts
def one_to_several(file_name, path_to_file='/path/to/save/', path_to_new_folder='/path/to/save/', delim='\n'):
    # Ensure the paths end with a slash
    path_to_file = os.path.join(path_to_file, '')
    path_to_new_folder = os.path.join(path_to_new_folder, '')

    # Create the folder for the split files
    create_dir(path_to_new_folder)

    # Open the source file and read its content
    with open(os.path.join(path_to_file, file_name), 'r', encoding='utf-8-sig') as f:
        all_text = f.read()
        # Split the content by the specified delimiter
        all_lines = all_text.split(delim)

    # Open a new file for writing the split content
    with open(os.path.join(path_to_new_folder, 'split_file.txt'), 'w', encoding='utf-8-sig') as f_new:
        # Write each non-empty line to the new file
        for line in all_lines:
            line = line.strip()
            if line == '':
                continue
            f_new.write(line + delim)

# Example usage of merging multiple files into one
several_to_one(
    new_file_name='merged_file.txt',  # Name for the merged file
    path_to_new_file='/path/to/save/',  # Directory to save the merged file
    path_to_folder='/path/to/files/',  # Directory containing the files to merge
    delim='\n'  # Delimiter to use between file contents
)

# Example usage of splitting a file into several parts
one_to_several(
    file_name='merged_file.txt',  # Name of the file to split
    path_to_file='/path/to/save/',  # Directory containing the file to split
    path_to_new_folder='/path/to/save/',  # Directory to save the split files
    delim='\n*****\n'  # Delimiter to separate parts of the file
)

# Print completion message
print('Done')
