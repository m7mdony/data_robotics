import os

def keep_last_n_files(directory, n):
    files = os.listdir(directory)
    files.sort()  # Sort the files alphabetically or based on your requirements

    # Make sure to handle the case where there are fewer than n files
    if len(files) <= n:
        print(f"There are fewer than {n} files in the directory. Nothing to delete.")
        return

    files_to_keep = files[-n:]

    for file_name in files:
        file_path = os.path.join(directory, file_name)
        # Delete files that are not in the list of files to keep
        if file_name not in files_to_keep:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Replace 'your_directory_path' with the actual path to your input directory
directory_path = 'images'

number_of_kept_files=1000   

# Replace 100 with the desired number of files to keep in the directory
keep_last_n_files(directory_path, 100)
