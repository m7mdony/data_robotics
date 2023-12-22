import os

def delete_non_txt_files(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Loop through each file
    for file in files:
        # Check if the file doesn't end with ".txt"
        
        if not file.endswith(".txt"):
            # Construct the full path to the file
            file_path = os.path.join(directory, file)
           
            # Delete the file
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Set the path to your input directory
input_dir = "labels"

#Call the function to delete non-.txt files
delete_non_txt_files(input_dir)
