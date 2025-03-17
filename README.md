# File_merger_and_splitter
## Description
This script provides functions to merge multiple text files into one and split a single file into several parts. It automates the process of file handling by reading, processing, and saving the files. The script is useful for efficiently managing large collections of text data that need to be consolidated or split for further analysis.

## Functional Description
The program performs the following tasks:
1. Merges multiple text files from a specified folder into one file.
2. Splits a single text file into multiple parts based on a delimiter.
3. Handles file creation and directory management for saving output files.

## How It Works
1. The script defines two main functions:
   - `several_to_one`: This function merges multiple text files into one. It reads each file, processes its content, and writes it into a new file.
   - `one_to_several`: This function splits a single text file into multiple parts, based on a specified delimiter.
2. It handles directory creation if the target folder does not exist.
3. Both functions allow customizing paths, file names, and delimiters for different file handling scenarios.

## Input Structure
To run the program, the following parameters need to be provided:
1. File paths: The folder containing the files to merge or split.
2. File names: The name of the output file after merging or splitting.
3. Delimiters: Define the character(s) that separate sections of the file for splitting.

## Technical Requirements
To run the program, the following are required:
1. Python 3.x
2. Installed library: os (standard Python library for file operations)

## Usage
1. Modify the paths and file names in the script as needed.
2. Run the script to either merge multiple text files into one or split a single file into several parts based on the defined delimiter.

## Example Output
After merging files:
- The output will be a single file that contains the combined text of all input files.

After splitting a file:
- The output will be a new file with the content split according to the delimiter.

## Conclusion
This script simplifies the process of merging and splitting text files, allowing for efficient management of large text datasets. It's particularly useful for preprocessing text data in data analysis and machine learning tasks.
