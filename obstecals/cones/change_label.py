import os
import fileinput

def update_classnum_to_zero(file_path):
    # Iterate through each line in the file and replace the first column with 0
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            data = line.split()
            if data:
                data[0] = '1'
                print(' '.join(data))
            else:
                print(line, end='')

def process_files_in_directory(directory):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if ".txt" in filename:
            file_path = os.path.join(directory, filename)
            update_classnum_to_zero(file_path)

# Specify the directory containing the txt files
input_directory = 'labels'

# Process files in the specified directory
process_files_in_directory(input_directory)
